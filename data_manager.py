import os
import time

class DataManager():
    def __init__(self):

        self.directory = "images"

        self.id = "None"
        self.speed = "None"
        self.rotate_speed = "None"
        self.date = "None"
        self.index = "None"

        self.brightness = "0"
        self.rotated_angle_z = "0"
        self.rotated_angle_x = "0"

        self.generate_main_folder()
    
    def generate_main_folder(self):
        os.makedirs(self.directory, exist_ok=True)

    def ask_example_info(self):
        while(True):
            id = input("Bitte geben Sie die Probe-ID: ")
            speed = input("Bitte Vorschubgeschwindigkeit eingeben:" )
            rotate_speed = input("Bitte Drehzahl eingeben: ")
            date = input("Bitte Datum eingeben: ")
            index = input("Bitte Index von Probe eingeben: ")
            print("Überprüfen bitte die Info ...")
            print("")
            print("Probe-ID = {}".format(id))
            print("Vorschubgeschwindigkeit = {}".format(speed))
            print("Drehzahl = {}".format(rotate_speed))
            print("Datum lautet: {}".format(date))
            print("Index: {}".format(index))
            print("")

            check = self.input_check()

            if check == "J":
                self.id = id
                self.speed = speed
                self.rotate_speed = rotate_speed
                self.index = index
                self.date = date
                break
            elif check == "N":
                print("")
                print("Bitte geb richtige Info ...")
                print("")
        self.write_example_info()
    
    def write_example_info(self):
        self.print_and_write_into_log("")
        self.print_and_write_into_log("start to chapture the images...")
        self.print_and_write_into_log("--------------------------------")
        self.print_and_write_into_log("probe-ID = {}".format(self.id))
        self.print_and_write_into_log("speed = {}".format(self.speed))
        self.print_and_write_into_log("rotate speed = {}".format(self.rotate_speed))
        self.print_and_write_into_log("date at: {}".format(self.date))
        self.print_and_write_into_log("index: {}".format(self.index))
        self.print_and_write_into_log("")

    def ask_brightness(self):
        self.brightness = self.input_brightness()

    def set_brightness(self, brightness):
        self.brightness = brightness
    
    def set_basic_info(self, dict_info):
        pass
    
    def print_and_write_into_log(self, text):
        text_line = time.strftime("%d.%m.%Y %R:%S") + ": " + text
        print(text)
        os.makedirs(self.directory, exist_ok=True)
        file_path = os.path.join(self.directory, "log.txt")
        file = open(file_path, 'a')
        file.write(text_line + '\n')
        file.close()

    def generate_label(self, x):
        label = '_'.join([self.index, str(round(x, 2)), str(self.brightness), self.rotated_angle_x, self.rotated_angle_z]) + ".jpg"
        return label
    
    def generate_image_path(self, x):
        folder_name = '_'.join([self.index, self.id, self.speed, self.rotate_speed])
        folder_path = os.path.join(self.directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        image_label = self.generate_label(x)
        image_path = os.path.join(folder_path, image_label)
        return image_path
    
    def set_rotate_angle_x(self, angle_x):
        self.rotated_angle_x = str(round(angle_x, 2))
        return angle_x
    
    def set_rotate_angle_z(self, angle_z):
        self.rotated_angle_z = str(round(angle_z, 2))
        return angle_z
    
    @staticmethod
    def input_check():
        while(True):
            check = input("Sind alle Info richtig? (J/N)")
            if check == 'J' or check == 'N':
                return check
            else:
                print("Falsche Eingabe, bitte versuch nochmal!")

    @staticmethod
    def input_brightness():
        while(True):
            brightness = input("Bitte die Heilligkeit eingeben: ")
            if brightness.isdigit():
                return brightness
            else:
                print("Falsche Eingabe, bitte versuch nochmal!")