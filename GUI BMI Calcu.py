import tkinter as tk
# import customtkinter as ctk   --if you using it you should erase comments in if operators and include command in libraries every algorithm

def calculate():
    weight = float(weigh_ent.get())
    height = float(weigh_ent.get())

    bmi = weight / (height ** 2)
    bmi = round(bmi, 1)

    if 18.5 > bmi:
        # result_lbl.config(text_color='blue') you free using custom colors
        result_var.set(f'Your BMI: {bmi}\nYour Rank: UnderWeight, \nYou need to gain the weight')

    if 24.9 >= bmi >= 18.5:
        # result_lbl.config(text_color='lightgreen') you free using custom colors
        result_var.set(f'Your BMI: {bmi}\nYour Rank: Normal, \nYou OK')
    
    if 29.9 >= bmi >= 25:
        # result_lbl.config(text_color='yellow') you free using custom colors
        result_var.set(f'Your BMI: {bmi}\nYour Rank: OverWeight, \nYou need to lose the weight')
    
    if 34.9 >= bmi >= 30:
        # result_lbl.config(text_color='orange') you free using custom colors
        result_var.set(f'Your BMI: {bmi}\nYour Rank: Obese, \nYou should lose the weight')

    if bmi > 35:
        # result_lbl.config(text_color='red') you free using custom colors
        result_var.set(f'Your BMI: {bmi}\nYour Rank: Extreme Obese, \nYou must lose the weight')

# ctk.set_appearance_mode('dark')
# ctk.set_default_color_theme('green') you free using custom colors

root = tk.Tk()
root.title('BMI Calculator From SEND') #You can change the title
root.geometry('355x255')
root.config(padx=20, pady=20)


weight_lbl = tk.Label(text='Weight (kg) :', pady=15)
height_lbl = tk.Label(text='Height (m) :', pady=15)

weight_lbl.grid(column= 0, row = 0)
height_lbl.grid(column = 0, row =1)

weigh_ent = tk.Entry()
height_ent = tk.Entry()

weigh_ent.grid(column = 1, row =0)
height_ent.grid(column = 1, row =1)

submit_butn = tk.Button(text='Submit', pady=15, command=calculate)
submit_butn.grid(columnspan=2, row=2)

result_var = tk.StringVar(value='')
result_lbl = tk.Label(textvariable=result_var,
                          font=('Arial',10),
)

result_lbl.grid(columnspan=3, row=3)

root.mainloop()