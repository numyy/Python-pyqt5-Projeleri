import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QMessageBox,
    QFormLayout, QDialog, QDialogButtonBox, QListWidgetItem, QFileDialog, QComboBox
)

class Ders:
    def __init__(self, ders_adi, icerik, ogretmen):
        self.ders_adi = ders_adi
        self.icerik = icerik
        self.ogretmen = ogretmen
        self.materyaller = []
        self.sorular = []

    def materyal_yukle(self, materyal):
        self.materyaller.append(materyal)

    def materyal_eris(self):
        return self.materyaller

    def soru_sor(self, soru, ogrenci):
        self.sorular.append(f"{ogrenci.isim} {ogrenci.soyad} tarafından sorulan soru: {soru}")

class Ogrenci:
    def __init__(self, isim, soyad, numara):
        self.isim = isim
        self.soyad = soyad
        self.numara = numara
        self.dersler = []

    def ders_ekle(self, ders):
        self.dersler.append(ders)

    def ders_cikar(self, ders):
        self.dersler.remove(ders)

    def soru_sor(self, ders, soru):
        ders.soru_sor(soru, self)

class Materyal:
    def __init__(self, materyal_adi, turu, icerik):
        self.materyal_adi = materyal_adi
        self.turu = turu
        self.icerik = icerik

    def icerik_goster(self):
        return self.icerik

class AddCourseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Yeni Ders Ekle')
        self.layout = QVBoxLayout()

        self.course_details = {
            "Matematik": {
                "Konular": ["Algebra", "Geometri", "Kalkülüs", "İstatistik"],
                "Öğretmenler": ["Ayşe Yılmaz", "Ali Veli", "Banu Kaya"]
            },
            "Türkçe": {
                "Konular": ["Edebiyat", "Dil Bilgisi", "Yazım Kuralları", "Okuma Teknikleri"],
                "Öğretmenler": ["Ahmet Erdem", "Elif Sinan", "Derya Can"]
            },
            "Fizik": {
                "Konular": ["Mekanik", "Elektromanyetizma", "Optik"],
                "Öğretmenler": ["Ali Demir", "Banu Yılmaz", "Cem Karaca"]
            },
            "Kimya": {
                "Konular": ["Atom Teorisi", "Periyodik Tablo", "Organik Kimya"],
                "Öğretmenler": ["Derya Deniz", "Efe Ay", "Fatma Çelik"]
            },
            "Biyoloji": {
                "Konular": ["Genetik", "Ekoloji", "Hücre Biyolojisi"],
                "Öğretmenler": ["Gökhan El", "Hakan İş", "Işıl Örnek"]
            },
            "Coğrafya": {
                "Konular": ["İklim Bilimi", "Kartografi", "Nüfus"],
                "Öğretmenler": ["Kemal Sun", "Lale Gün", "Mehmet Can"]
            },
            "Tarih": {
                "Konular": ["Dünya Tarihi", "Osmanlı Tarihi", "Çağdaş Tarih"],
                "Öğretmenler": ["Nalan Kaya", "Orhan Gencebay", "Pelin Ay"]
            },
            "Felsefe": {
                "Konular": ["Etik", "Estetik", "Mantık"],
                "Öğretmenlers": ["Rıza Bey", "Seda Vural", "Tayfun Uzun"]
            }
        }

        form_layout = QFormLayout()
        self.course_name_input = QComboBox()
        self.course_name_input.addItems(self.course_details.keys())
        self.content_input = QComboBox()
        self.teacher_input = QComboBox()

        self.update_course_details()

        self.course_name_input.currentTextChanged.connect(self.update_course_details)

        form_layout.addRow("Ders Adı:", self.course_name_input)
        form_layout.addRow("İçerik:", self.content_input)
        form_layout.addRow("Öğretmen:", self.teacher_input)

        self.layout.addLayout(form_layout)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        self.layout.addWidget(self.buttons)
        self.setLayout(self.layout)

    def update_course_details(self):
        course_name = self.course_name_input.currentText()
        details = self.course_details[course_name]

        self.content_input.clear()
        self.content_input.addItems(details["Konular"])

        self.teacher_input.clear()
        self.teacher_input.addItems(details["Öğretmenler"])

    def get_details(self):
        return {
            'course_name': self.course_name_input.currentText(),
            'content': self.content_input.currentText(),
            'teacher': self.teacher_input.currentText()
        }

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eğitim Materyali Paylaşım Platformu")
        self.setGeometry(100, 100, 800, 500)  # Reduced window size for better layout

        self.courses = []
        self.students = []
        self.current_student = None

        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        student_layout = QVBoxLayout()

        self.details_text = QTextEdit()
        self.details_text.setReadOnly(True)
        self.details_text.setMaximumHeight(150)  # Reduced the size of the large text box

        main_layout.addWidget(self.details_text)

        self.student_name_input = QLineEdit()
        self.student_surname_input = QLineEdit()
        self.student_number_input = QLineEdit()
        self.register_button = QPushButton("Öğrenci Kaydet")
        self.register_button.clicked.connect(self.register_student)

        student_layout.addWidget(QLabel("Öğrenci Adı:"))
        student_layout.addWidget(self.student_name_input)
        student_layout.addWidget(QLabel("Öğrenci Soyadı:"))
        student_layout.addWidget(self.student_surname_input)
        student_layout.addWidget(QLabel("Öğrenci Numarası:"))
        student_layout.addWidget(self.student_number_input)
        student_layout.addWidget(self.register_button)

        self.soru_gonder_button = QPushButton("Soru Sor")
        self.soru_gonder_button.clicked.connect(self.send_question)
        self.soru_gonder_button.setEnabled(False)  # Initially disabled

        self.add_course_button = QPushButton("Ders Ekle")
        self.add_course_button.clicked.connect(self.add_course)

        self.upload_button = QPushButton("Karşıya Yükle")
        self.upload_button.clicked.connect(self.upload_material)

        button_layout.addWidget(self.add_course_button)
        button_layout.addWidget(self.upload_button)
        button_layout.addWidget(self.soru_gonder_button)

        main_layout.addLayout(student_layout)
        main_layout.addLayout(button_layout)
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def add_course(self):
        dialog = AddCourseDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            details = dialog.get_details()
            new_course = Ders(details['course_name'], details['content'], details['teacher'])
            self.courses.append(new_course)
            self.update_details_text()
            QMessageBox.information(self, "Ders Ekleme", f"'{details['course_name']}' adlı ders başarıyla eklendi!")
            self.soru_gonder_button.setEnabled(True)

    def update_details_text(self):
        if self.courses:
            course = self.courses[-1]
            self.details_text.setText(f"Ders Adı: {course.ders_adi}\nİçerik: {course.icerik}\nÖğretmen: {course.ogretmen}")

    def upload_material(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Materyal Yükle", "", "All Files (*);;PDF Files (*.pdf);;Text Files (*.txt)")
        if file_path:
            materyal_adi = file_path.split('/')[-1]
            current_course = self.courses[-1] if self.courses else None
            if current_course:
                current_course.materyal_yukle(Materyal(materyal_adi, "Dosya", file_path))
                self.details_text.append(f"Yüklenen Materyal: {materyal_adi}")
                QMessageBox.information(self, "Materyal Yükleme", f"'{materyal_adi}' başarıyla yüklendi!")

    class AskQuestionDialog(QDialog):
        def __init__(self, courses, parent=None):
            super().__init__(parent)
            self.setWindowTitle('Soru Sor')
            self.layout = QVBoxLayout()

            form_layout = QFormLayout()
            self.course_input = QComboBox()
            self.course_input.addItems(courses)
            self.question_input = QTextEdit()

            form_layout.addRow("Ders Adı:", self.course_input)
            form_layout.addRow("Sorunuz:", self.question_input)

            self.layout.addLayout(form_layout)
            buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            buttons.accepted.connect(self.accept)
            buttons.rejected.connect(self.reject)

            self.layout.addWidget(buttons)
            self.setLayout(self.layout)

        def get_details(self):
            return {
                'course': self.course_input.currentText(),
                'question': self.question_input.toPlainText()
            }

    def send_question(self):
        if not self.current_student:
            QMessageBox.warning(self, "Hata", "Öğrenci bilgisi eksik, lütfen önce bir öğrenci kaydedin.")
            return
        if not self.courses:
            QMessageBox.warning(self, "Hata", "Kurs listesi boş, lütfen önce bir ders ekleyin.")
            return

        course_names = [course.ders_adi for course in self.courses]

        try:
            dialog = AskQuestionDialog(course_names, self)
            if dialog.exec_() == QDialog.Accepted:
                details = dialog.get_details()
                selected_course = next((course for course in self.courses if course.ders_adi == details['course']),
                                       None)
                if not selected_course:
                    QMessageBox.warning(self, "Hata", "Seçilen kurs bulunamadı.")
                    return

                selected_course.soru_sor(details['question'], self.current_student)
                self.details_text.append(f"Sorulan Soru: {details['question']}")
                QMessageBox.information(self, "Başarılı", "Sorunuz başarıyla gönderildi!")
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Bir hata oluştu: {str(e)}")
            return

    def register_student(self):
        name = self.student_name_input.text()
        surname = self.student_surname_input.text()
        number = self.student_number_input.text()
        if name and surname and number:
            new_student = Ogrenci(name, surname, number)
            self.students.append(new_student)
            self.current_student = new_student
            self.student_name_input.clear()
            self.student_surname_input.clear()
            self.student_number_input.clear()
            self.details_text.setText(f"Hoşgeldin {name} {surname}!")
            QMessageBox.information(self, "Öğrenci Kayıt", f"Hoşgeldin {name} {surname}!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
