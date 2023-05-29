from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox)
from ui_login import Ui_Login
import sys
from ui_scan import Ui_MainWindow
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QTimer, QDateTime
import win32com.client
import os
import pytesseract
from PIL import Image,ImageQt
from databases import MongoDB
import io



class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle('Login do Sistema')

        self.btn_login.clicked.connect(self.checkLogin)

    
    def checkLogin(self):

        self.users = MongoDB('root','root','digitalizador_pi')
        self.users.connect()
        autenticado = self.users.check_user(self.txt_user.text(),self.txt_password.text())

        if autenticado == "Administrador" or autenticado == "Usuário":
            self.w = MainWindow(autenticado)
            self.w.show()
            self.close()

        else:

            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Login ou senha incorreto \n \n Tentativa:{self.tentativas +1} de 3')
                msg.exec_()
                self.tentativas += 1
            if self.tentativas == 3:
                self.users.close()
                sys.exit(0)



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,user) -> None:
        super(MainWindow, self).__init__()
        
        self.setupUi(self)
        self.setWindowTitle('Digitalizador P.I')
        self.entry_datavenda.setText(QDateTime.currentDateTime().toString("dd/MM/yyyy HH:mm:ss"))
        if user == "Usuário":
            self.btn_cadastrar_user.setVisible(False)

        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.home))
        self.btn_cvendas.clicked.connect(lambda:self.Pages.setCurrentWidget(self.Cad_vendas))
        self.btn_cadastrar_user.clicked.connect(lambda: self.Pages.setCurrentWidget(self.tela_cadastro))
        self.btn_EscanearDoc.clicked.connect(lambda: self.Pages.setCurrentWidget(self.EscanearDoc))
               
        self.btn_cadastrar.clicked.connect(self.subscribe_user)
        self.btn_enviarcad.clicked.connect(self.subscribe_clients)
        self.btn_consultas.clicked.connect(self.download_clients)


        
       

        # adiciona conexões para os botões e labels correspondentes
        self.btn_digitalizarTab1.clicked.connect(lambda: self.scan_document(self.label_scan1,'cupom'))
        self.btn_digitalizarTab2.clicked.connect(lambda: self.scan_document(self.label_scan2,'frente_receita'))
        self.btn_digitalizarTab3.clicked.connect(lambda: self.scan_document(self.label_scan3,'verso_receita'))
        self.btn_digitalizarTab4.clicked.connect(lambda: self.scan_document(self.label_scan4,'documento'))
        self.btn_digitalizarTab5.clicked.connect(lambda: self.scan_document(self.label_scan5,'frente_procuração'))
        self.btn_digitalizarTab6.clicked.connect(lambda: self.scan_document(self.label_scan6,'verso_procuração'))

        self.btn_ocrTab1.clicked.connect(lambda: self.convert_image_to_text_and_show(self.label_scan1))
        self.btn_ocrTab2.clicked.connect(lambda: self.convert_image_to_text_and_show(self.label_scan2))
        self.btn_ocrTab3.clicked.connect(lambda: self.convert_image_to_text_and_show(self.label_scan3))
        self.btn_ocrTab4.clicked.connect(lambda: self.convert_image_to_text_and_show(self.label_scan4))
        self.btn_ocrTab5.clicked.connect(lambda: self.convert_image_to_text_and_show(self.label_scan5))
        self.btn_ocrTab6.clicked.connect(lambda: self.convert_image_to_text_and_show(self.label_scan6))

    def subscribe_user(self):

        if self.entry_senha.text() != self.entry_csenha.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("ADVERTÊNCIA")
            msg.setText("As senhas não são iguais!!!")
            msg.exec_()
            return None
        nome = self.entry_nome.text()
        user = self.entry_user.text()
        password = self.entry_senha.text()
        access = self.perfil_box.currentText()

        mongo = MongoDB('root', 'root', 'digitalizador_pi')
        mongo.connect()
        mongo.insert_user(nome, user, password, access)
        mongo.close()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Cadastro de Usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

        self.entry_nome.setText("")
        self.entry_user.setText("")
        self.entry_senha.setText("")
        self.entry_csenha.setText("")

    def subscribe_clients(self):
        global cpf, data_venda, auto_ms, num_coo
        
        num_coo = int(self.entry_numerocoo.text())
        cpf = self.entry_cpf.text()
        auto_ms = int(self.entry_automs.text())
        data_venda = self.entry_datavenda.text()
        

        mongo = MongoDB('root', 'root', 'digitalizador_pi')
        mongo.connect()
        mongo.insert_client(num_coo, cpf, auto_ms, data_venda)
        mongo.create_collection_clients(cpf)
        mongo.close()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Cadastro de Usuário")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

    
    def download_clients(self):
        CPF = self.entry_cpf.text()
        NUM_coo = self.entry_numerocoo.text()
        AUTO_ms = self.entry_automs.text()

        if CPF == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Consulta de Usuário")
            msg.setText("Preencha o Campo CPF!")
            msg.exec_()  
            return  

        if NUM_coo == "":
            NUM_coo = "null"
        
        if AUTO_ms == "":
            AUTO_ms = "null"
                    

        mongo = MongoDB('root', 'root', 'digitalizador_pi')
        mongo.connect()
        documento = mongo.get_doc(NUM_coo, CPF, AUTO_ms)
        mongo.close()

        if documento:
            # Exibir os valores nas QLineEdits correspondentes
            self.entry_cpf.setText(documento.get("cpf", ""))
            self.entry_numerocoo.setText(str(documento.get("numero_coo", "")))
            self.entry_automs.setText(str(documento.get("Auto_Ms", "")))
            self.entry_datavenda.setText(documento.get("Data_venda", ""))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Atenção")
            msg.setText("Documento não encontrado!!!")
            msg.exec_()

               
    def scan_document(self, label,tab_doc):
        global img, cpf, img_tk, img_width, img_height
        cpf = self.entry_cpf.text()
        wia = win32com.client.Dispatch("WIA.CommonDialog")
        self.image = wia.ShowAcquireImage()

        # cria um nome de arquivo para a imagem digitalizada
        self.image_path = r"C:/Users/Keny/Documents/testscan/img.jpg"
        self.file_exists = os.path.isfile(self.image_path)
        if self.file_exists:
            self.file_count = 1
            while self.file_exists:
                self.file_count += 1
                self.new_image_path = r"C:/Users/Keny/Documents/testscan/img" + str(self.file_count) + ".jpg"
                self.file_exists = os.path.isfile(self.new_image_path)
            self.image_path = self.new_image_path

        self.image.SaveFile(self.image_path)

        # converte a imagem para pdf
        with io.BytesIO() as output:
            with Image.open(self.image_path) as img:
                img.save(output, format='pdf')
            # salva o arquivo pdf
            pdf_bytes = output.getvalue()
            with open(self.image_path[:-3] + "pdf", 'wb') as f:
                f.write(pdf_bytes)
            pdf = pdf_bytes

        # atualiza o label com o arquivo digitalizado
        pixmap = QPixmap(self.image_path)
        label.setPixmap(pixmap)

        mongo = MongoDB('root', 'root', 'digitalizador_pi')
        mongo.connect()
        mongo.insert_pdf(pdf, tab_doc)
       
        mongo.close()
       
    def convert_image_to_text_and_show(self, label):
        # Get the image from the label
        self.qimage = label.pixmap().toImage()
        self.image = ImageQt.fromqimage(self.qimage)

        # Save the image to a temporary file in TIFF format
        temp_image_path = "temp.tiff"
        self.image.save(temp_image_path)

        # Define Tesseract executable path and language data directory
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
        os.environ['TESSDATA_PREFIX'] = r'C:/Program Files/Tesseract-OCR/tessdata'

        # Convert the image to text with higher quality settings
        convert_command = (
            f'convert -quality 100 -density 300 -depth 8 -strip -background white -alpha off {temp_image_path} {temp_image_path}'
        )
        os.system(convert_command)

        # Run Tesseract OCR on the converted image
        ocr_command = (
            f'tesseract {temp_image_path} tabela-assessores -l por+por_best -c preserve_interword_spaces=1'
        )
        os.system(ocr_command)

        # Read the extracted text from the output file
        output_file_path = "tabela-assessores.txt"
        with open(output_file_path, "r", encoding="utf-8") as file:
            self.text = file.read()

        # Display the text in the Windows text editor
        os.system(f"notepad.exe {output_file_path}")

        # Delete temporary files
        os.remove(temp_image_path)
        os.remove(output_file_path)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
