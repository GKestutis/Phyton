import tkinter as tk

class Skaiciuotuvas:
	def __init__(self):
		self.sukurk_langa()
		self.sukurk_virsutine_eilute()
		self.sukurk_mygtukus()

	def sukurk_langa(self):
		self.langas = tk.Tk()
		self.langas.title('Skaiciuotuvas')

	def sukurk_virsutine_eilute(self):
		self.eilutes_tekstas = tk.StringVar()
		eilute = tk.Label(self.langas, textvariable=self.eilutes_tekstas)
		eilute.grid(row=0, column=0, columnspan=5)

	def sukurk_mygtukus(self):
		mygtukas0 = tk.Button(self.langas, text='0', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '0'))
		mygtukas1 = tk.Button(self.langas, text='1', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '1'))
		mygtukas2 = tk.Button(self.langas, text='2', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '2'))
		mygtukas3 = tk.Button(self.langas, text='3', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '3'))
		mygtukas4 = tk.Button(self.langas, text='4', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '4'))
		mygtukas5 = tk.Button(self.langas, text='5', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '5'))
		mygtukas6 = tk.Button(self.langas, text='6', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '6'))
		mygtukas7 = tk.Button(self.langas, text='7', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '7'))
		mygtukas8 = tk.Button(self.langas, text='8', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '8'))
		mygtukas9 = tk.Button(self.langas, text='9', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '9'))

		mygtukas_k_skliaustas = tk.Button(self.langas, text='(', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '('))
		mygtukas_d_skliaustas = tk.Button(self.langas, text=')', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + ')'))

		mygtukas_plius = tk.Button(self.langas, text='+', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '+'))
		mygtukas_minus = tk.Button(self.langas, text='-', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '-'))
		mygtukas_daugyba = tk.Button(self.langas, text='*', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '*'))
		mygtukas_dalyba = tk.Button(self.langas, text='/', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '/'))

		mygtukas_taskas = tk.Button(self.langas, text='.', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get() + '.'))

		mygtukas_trinti = tk.Button(self.langas, text='⌫', command=lambda: self.eilutes_tekstas.set(self.eilutes_tekstas.get()[:-1]))
		mygtukas_viska_trinti = tk.Button(self.langas, text='C', command=lambda: self.eilutes_tekstas.set(''))

		mygtukas_lygu = tk.Button(self.langas, text='=', command=self.skaiciuok)

		mygtukas7.grid(row=1, column=0)
		mygtukas8.grid(row=1, column=1)
		mygtukas9.grid(row=1, column=2)
		mygtukas_k_skliaustas.grid(row=1, column=3)
		mygtukas_d_skliaustas.grid(row=1, column=4)

		mygtukas4.grid(row=2, column=0)
		mygtukas5.grid(row=2, column=1)
		mygtukas6.grid(row=2, column=2)
		mygtukas_plius.grid(row=2, column=3)
		mygtukas_minus.grid(row=2, column=4)

		mygtukas1.grid(row=3, column=0)
		mygtukas2.grid(row=3, column=1)
		mygtukas3.grid(row=3, column=2)
		mygtukas_daugyba.grid(row=3, column=3)
		mygtukas_dalyba.grid(row=3, column=4)

		mygtukas0.grid(row=4, column=0)
		mygtukas_taskas.grid(row=4, column=1)
		mygtukas_trinti.grid(row=4, column=2)
		mygtukas_viska_trinti.grid(row=4, column=3)
		mygtukas_lygu.grid(row=4, column=4)

	def skaiciuok(self):
		try:
			x = eval(self.eilutes_tekstas.get())
			self.eilutes_tekstas.set(str(x))
		except (ZeroDivisionError, SyntaxError):
			self.eilutes_tekstas.set('')

	def pagrindinis_ciklas(self):
		self.langas.mainloop()

if __name__ == '__main__':
	skaiciuotuvas = Skaiciuotuvas()
	skaiciuotuvas.pagrindinis_ciklas()
