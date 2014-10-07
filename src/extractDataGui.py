import Tkinter
import tkFileDialog, tkMessageBox

class applicationGUI:
	def __init__(self, root):
		self.root = root
		self.initialisation()
	
	def initialisation(self):
		Tkinter.Label(self.root, text="Hello, world!").grid(column=0, row=0)
		Tkinter.Button(self.root, text='Indiquer le fichier',
					command=(lambda: renseignerFichier(self.root))).grid(column=0, row=1)


def renseignerFichier(root):
	nomFichier = tkFileDialog.askopenfilename(parent=root, title='Nom du fichier satellite')
	#return nomFichier
	tkMessageBox.showinfo('Fichier', nomFichier)

def main():
	root = Tkinter.Tk()
	root.title('My application')
	app = applicationGUI(root)
	#fichier = tkFileDialog.askopenfile(parent=root, mode='rb', title='Selectionner un fichier')
	root.mainloop()

if __name__ == "__main__":
	main()
