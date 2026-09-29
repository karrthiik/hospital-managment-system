import tkinter as tk
from tkinter import messagebox, ttk

doctors = [
    {"name": "Dr. Sarah", "specialization": "Cardiology", "phone": "9876543210"},
    {"name": "Dr. Rajesh", "specialization": "Neurology", "phone": "9876543211"},
    {"name": "Dr. Emily", "specialization": "Pediatrics", "phone": "9876543212"},
    {"name": "Dr. Michael", "specialization": "Orthopedics", "phone": "9876543213"},
    {"name": "Dr. Priya", "specialization": "Dermatology", "phone": "9876543214"}
]

patients = [
    {"name": "Alice", "age": "29", "gender": "Female", "phone": "9123456780"},
    {"name": "Robert", "age": "45", "gender": "Male", "phone": "9123456781"},
    {"name": "Sneha", "age": "34", "gender": "Female", "phone": "9123456782"},
    {"name": "David", "age": "58", "gender": "Male", "phone": "9123456783"},
    {"name": "Roy", "age": "12", "gender": "Female", "phone": "9123456784"}
]

appointments = [
    {
        "patient": "Alice",
        "doctor": "Dr. Sarah",
        "date": "2026-10-05",
        "time": "10:30 AM",
        "reason": "Routine Heart Checkup"
    },
    {
        "patient": "Robert",
        "doctor": "Dr. Michael",
        "date": "2026-10-06",
        "time": "02:00 PM",
        "reason": "Knee Pain Consultation"
    },
    {
        "patient": "Sneha",
        "doctor": "Dr. Priya",
        "date": "2026-10-07",
        "time": "11:15 AM",
        "reason": "Skin Allergy Treatment"
    }
]

username = "admin"
password = "1234"

def login():
    if username_entry.get() == username and password_entry.get() == password:
        login_window.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


login_window = tk.Tk()
login_window.title("Hospital Management System - Login")
login_window.geometry("400x300")

tk.Label(
    login_window,
    text="Hospital Management System",
    font=("Arial", 18, "bold")
).pack(pady=30)

tk.Label(login_window, text="Username").pack()
username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)

tk.Label(login_window, text="Password").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=5)

tk.Button(
    login_window,
    text="Login",
    width=15,
    command=login
).pack(pady=20)

def open_dashboard():

    dashboard = tk.Tk()
    dashboard.title("Hospital Management System")
    dashboard.geometry("700x500")

    tk.Label(
        dashboard,
        text="Hospital Management System",
        font=("Arial", 24, "bold")
    ).pack(pady=30)

    tk.Button(
        dashboard,
        text="Doctor Management",
        width=25,
        command=doctor_window
    ).pack(pady=10)

    tk.Button(
        dashboard,
        text="Patient Management",
        width=25,
        command=patient_window
    ).pack(pady=10)

    tk.Button(
        dashboard,
        text="Appointment Booking",
        width=25,
        command=appointment_window
    ).pack(pady=10)

    tk.Button(
        dashboard,
        text="View Appointments",
        width=25,
        command=view_appointments
    ).pack(pady=10)

    dashboard.mainloop()

def doctor_window():

    window = tk.Toplevel()
    window.title("Doctor Management")
    window.geometry("500x500")

    tk.Label(
        window,
        text="Doctor Management",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    doctor_presets = {
        "Dr. Sarah": {"specialization": "Cardiology", "phone": "9876543210"},
        "Dr. Rajesh": {"specialization": "Neurology", "phone": "9876543211"},
        "Dr. Emily": {"specialization": "Pediatrics", "phone": "9876543212"},
        "Dr. Michael": {"specialization": "Orthopedics", "phone": "9876543213"},
        "Dr. Priya": {"specialization": "Dermatology", "phone": "9876543214"}
    }

    tk.Label(window, text="Select / Enter Doctor Name").pack()
    name_entry = ttk.Combobox(window, values=list(doctor_presets.keys()), width=30)
    name_entry.pack(pady=5)

    tk.Label(window, text="Select / Enter Specialization").pack()
    specializations = [
        "Cardiology", "Neurology", "Pediatrics", "Orthopedics",
        "Dermatology", "General Medicine", "Gynecology", "Oncology",
        "ENT", "Ophthalmology", "Psychiatry", "Radiology"
    ]
    specialization_entry = ttk.Combobox(window, values=specializations, width=30)
    specialization_entry.pack(pady=5)

    tk.Label(window, text="Phone").pack()
    phone_entry = tk.Entry(window, width=33)
    phone_entry.pack(pady=5)

    def on_doctor_select(event):
        selected = name_entry.get()
        if selected in doctor_presets:
            specialization_entry.set(doctor_presets[selected]["specialization"])
            phone_entry.delete(0, tk.END)
            phone_entry.insert(0, doctor_presets[selected]["phone"])

    name_entry.bind("<<ComboboxSelected>>", on_doctor_select)

    def add_doctor():

        name = name_entry.get()
        specialization = specialization_entry.get()
        phone = phone_entry.get()

        if name == "" or specialization == "":
            messagebox.showwarning(
                "Warning",
                "Please enter doctor details"
            )
            return

        doctor = {
            "name": name,
            "specialization": specialization,
            "phone": phone
        }

        doctors.append(doctor)

        messagebox.showinfo(
            "Success",
            "Doctor added successfully"
        )

        name_entry.set("")
        specialization_entry.set("")
        phone_entry.delete(0, tk.END)

    tk.Button(
        window,
        text="Add Doctor",
        width=20,
        command=add_doctor
    ).pack(pady=15)

    tk.Button(
        window,
        text="View Doctors",
        width=20,
        command=view_doctors
    ).pack(pady=5)

def view_doctors():

    window = tk.Toplevel()
    window.title("Doctors")
    window.geometry("600x400")

    tk.Label(
        window,
        text="Doctor List",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    if len(doctors) == 0:
        tk.Label(
            window,
            text="No doctors added"
        ).pack()
        return

    for i, doctor in enumerate(doctors, start=1):

        text = (
            f"{i}. {doctor['name']} | "
            f"{doctor['specialization']} | "
            f"{doctor['phone']}"
        )

        tk.Label(
            window,
            text=text,
            font=("Arial", 12)
        ).pack(pady=5)


def patient_window():

    window = tk.Toplevel()
    window.title("Patient Management")
    window.geometry("500x550")

    tk.Label(
        window,
        text="Patient Management",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    patient_presets = {
        "Alice": {"age": "29", "gender": "Female", "phone": "9123456780"},
        "Robert": {"age": "45", "gender": "Male", "phone": "9123456781"},
        "Sneha": {"age": "34", "gender": "Female", "phone": "9123456782"},
        "David": {"age": "58", "gender": "Male", "phone": "9123456783"},
        "Roy": {"age": "12", "gender": "Female", "phone": "9123456784"}
    }

    tk.Label(window, text="Select / Enter Patient Name").pack()
    name_entry = ttk.Combobox(window, values=list(patient_presets.keys()), width=30)
    name_entry.pack(pady=5)

    tk.Label(window, text="Select / Enter Age").pack()
    age_entry = ttk.Combobox(window, values=[str(a) for a in range(1, 101)], width=30)
    age_entry.pack(pady=5)

    tk.Label(window, text="Select Gender").pack()
    gender_entry = ttk.Combobox(window, values=["Female", "Male", "Other"], state="readonly", width=30)
    gender_entry.pack(pady=5)

    tk.Label(window, text="Phone").pack()
    phone_entry = tk.Entry(window, width=33)
    phone_entry.pack(pady=5)

    def on_patient_select(event):
        selected = name_entry.get()
        if selected in patient_presets:
            age_entry.set(patient_presets[selected]["age"])
            gender_entry.set(patient_presets[selected]["gender"])
            phone_entry.delete(0, tk.END)
            phone_entry.insert(0, patient_presets[selected]["phone"])

    name_entry.bind("<<ComboboxSelected>>", on_patient_select)

    def add_patient():

        name = name_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()
        phone = phone_entry.get()

        if name == "" or age == "":
            messagebox.showwarning(
                "Warning",
                "Please enter patient details"
            )
            return

        patient = {
            "name": name,
            "age": age,
            "gender": gender,
            "phone": phone
        }

        patients.append(patient)

        messagebox.showinfo(
            "Success",
            "Patient added successfully"
        )

        name_entry.set("")
        age_entry.set("")
        gender_entry.set("")
        phone_entry.delete(0, tk.END)

    tk.Button(
        window,
        text="Add Patient",
        width=20,
        command=add_patient
    ).pack(pady=15)

    tk.Button(
        window,
        text="View Patients",
        width=20,
        command=view_patients
    ).pack(pady=5)

def view_patients():

    window = tk.Toplevel()
    window.title("Patients")
    window.geometry("600x400")

    tk.Label(
        window,
        text="Patient List",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    if len(patients) == 0:
        tk.Label(
            window,
            text="No patients added"
        ).pack()
        return

    for i, patient in enumerate(patients, start=1):

        text = (
            f"{i}. {patient['name']} | "
            f"Age: {patient['age']} | "
            f"{patient['gender']} | "
            f"{patient['phone']}"
        )

        tk.Label(
            window,
            text=text,
            font=("Arial", 12)
        ).pack(pady=5)


def appointment_window():

    window = tk.Toplevel()
    window.title("Book Appointment")
    window.geometry("520x620")

    tk.Label(
        window,
        text="Book Appointment",
        font=("Arial", 20, "bold")
    ).pack(pady=15)

    patient_type_var = tk.StringVar(value="registered")

    type_frame = tk.Frame(window)
    type_frame.pack(pady=5)

    tk.Label(type_frame, text="Patient Type: ", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)

    patient_container = tk.Frame(window)
    patient_container.pack(pady=5)

    patient_label = tk.Label(patient_container, text="Select Registered Patient")
    patient_label.pack()

    patient_names = [f"{p['name']} (Age: {p['age']})" for p in patients] if patients else ["No registered patients"]
    patient_combobox = ttk.Combobox(patient_container, values=patient_names, state="readonly", width=33)
    if patients:
        patient_combobox.current(0)
    patient_combobox.pack(pady=3)

    outside_label = tk.Label(patient_container, text="Outside Patient Name")
    outside_entry = tk.Entry(patient_container, width=35)

    outside_phone_label = tk.Label(patient_container, text="Outside Patient Phone (Optional)")
    outside_phone_entry = tk.Entry(patient_container, width=35)

    def toggle_patient_type():
        if patient_type_var.get() == "registered":
            outside_label.pack_forget()
            outside_entry.pack_forget()
            outside_phone_label.pack_forget()
            outside_phone_entry.pack_forget()

            patient_label.pack()
            patient_combobox.pack(pady=3)
        else:
            patient_label.pack_forget()
            patient_combobox.pack_forget()

            outside_label.pack()
            outside_entry.pack(pady=3)
            outside_phone_label.pack()
            outside_phone_entry.pack(pady=3)

    rb_reg = tk.Radiobutton(
        type_frame,
        text="Registered Patient",
        variable=patient_type_var,
        value="registered",
        command=toggle_patient_type
    )
    rb_reg.pack(side=tk.LEFT, padx=5)

    rb_out = tk.Radiobutton(
        type_frame,
        text="Outside Patient",
        variable=patient_type_var,
        value="outside",
        command=toggle_patient_type
    )
    rb_out.pack(side=tk.LEFT, padx=5)

    tk.Label(window, text="Select Doctor").pack(pady=(10, 0))
    doctor_names = [f"{d['name']} - {d['specialization']}" for d in doctors] if doctors else ["No doctors available"]
    doctor_combobox = ttk.Combobox(window, values=doctor_names, state="readonly", width=33)
    if doctors:
        doctor_combobox.current(0)
    doctor_combobox.pack(pady=5)

    tk.Label(window, text="Date (e.g. 2026-10-15)").pack()
    date_entry = tk.Entry(window, width=35)
    date_entry.pack(pady=5)

    tk.Label(window, text="Time (e.g. 10:30 AM)").pack()
    time_entry = tk.Entry(window, width=35)
    time_entry.pack(pady=5)

    tk.Label(window, text="Reason").pack()
    reason_entry = tk.Entry(window, width=35)
    reason_entry.pack(pady=5)

    def book_appointment():

        if not doctors:
            messagebox.showwarning(
                "Warning",
                "Please make sure at least one doctor exists before booking."
            )
            return

        if patient_type_var.get() == "registered":
            if not patients:
                messagebox.showwarning(
                    "Warning",
                    "No registered patients available. Please select Outside Patient or add patients."
                )
                return
            patient = patient_combobox.get()
        else:
            outside_name = outside_entry.get().strip()
            if outside_name == "":
                messagebox.showwarning(
                    "Warning",
                    "Please enter the outside patient's name."
                )
                return
            outside_phone = outside_phone_entry.get().strip()
            if outside_phone:
                patient = f"{outside_name} (Outside - {outside_phone})"
            else:
                patient = f"{outside_name} (Outside Patient)"

        doctor = doctor_combobox.get()
        date = date_entry.get().strip()
        time = time_entry.get().strip()
        reason = reason_entry.get().strip()

        if patient == "" or doctor == "" or date == "":
            messagebox.showwarning(
                "Warning",
                "Please select/enter patient, doctor and enter date"
            )
            return

        appointment = {
            "patient": patient,
            "doctor": doctor,
            "date": date,
            "time": time,
            "reason": reason
        }

        appointments.append(appointment)

        messagebox.showinfo(
            "Success",
            "Appointment booked successfully"
        )

        outside_entry.delete(0, tk.END)
        outside_phone_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
        reason_entry.delete(0, tk.END)

    tk.Button(
        window,
        text="Book Appointment",
        width=20,
        command=book_appointment
    ).pack(pady=20)

def view_appointments():

    window = tk.Toplevel()
    window.title("Appointments")
    window.geometry("700x450")

    tk.Label(
        window,
        text="Appointment List",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    if len(appointments) == 0:
        tk.Label(
            window,
            text="No appointments booked"
        ).pack()
        return

    for i, appointment in enumerate(appointments, start=1):

        text = (
            f"{i}. Patient: {appointment['patient']} | "
            f"Doctor: {appointment['doctor']} | "
            f"Date: {appointment['date']} | "
            f"Time: {appointment['time']} | "
            f"Reason: {appointment['reason']}"
        )

        tk.Label(
            window,
            text=text,
            font=("Arial", 11)
        ).pack(pady=5)


login_window.mainloop()