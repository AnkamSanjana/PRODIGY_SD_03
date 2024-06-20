class Contact:
  def __init__(self, name, phone, email):
    self.name = name
    self.phone = phone
    self.email = email

class ContactManager:
  def __init__(self):
    self.contacts = []

  def add_contact(self):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact = Contact(name, phone, email)
    self.contacts.append(contact)
    print("Contact added successfully!")

  def view_contacts(self):
    if not self.contacts:
      print("Contact list is empty.")
      return
    for i, contact in enumerate(self.contacts):
      print(f"{i+1}. {contact.name} - {contact.phone} - {contact.email}")

  def edit_contact(self):
    self.view_contacts()
    if not self.contacts:
      return
    index = int(input("Enter the number of the contact to edit: ")) - 1
    if 0 <= index < len(self.contacts):
      contact = self.contacts[index]
      print(f"Current details: {contact.name} - {contact.phone} - {contact.email}")
      new_name = input("Enter new name (leave blank to keep current): ")
      new_phone = input("Enter new phone number (leave blank to keep current): ")
      new_email = input("Enter new email address (leave blank to keep current): ")
      if new_name:
        contact.name = new_name
      if new_phone:
        contact.phone = new_phone
      if new_email:
        contact.email = new_email
      print("Contact updated successfully!")
    else:
      print("Invalid contact number.")

  def delete_contact(self):
    self.view_contacts()
    if not self.contacts:
      return
    index = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= index < len(self.contacts):
      del self.contacts[index]
      print("Contact deleted successfully!")
    else:
      print("Invalid contact number.")

  def load_contacts(self, filename):
    try:
      with open(filename, "r") as file:
        for line in file:
          name, phone, email = line.strip().split(",")
          contact = Contact(name, phone, email)
          self.contacts.append(contact)
      print("Contacts loaded from file.")
    except FileNotFoundError:
      print("File not found. Starting with an empty contact list.")

  def save_contacts(self, filename):
    with open(filename, "w") as file:
      for contact in self.contacts:
        file.write(f"{contact.name},{contact.phone},{contact.email}\n")
    print("Contacts saved to file.")

def main():
  manager = ContactManager()
  manager.load_contacts("contacts.txt")

  while True:
    print("\nContact Management System:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Save Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      manager.add_contact()
    elif choice == "2":
      manager.view_contacts()
    elif choice == "3":
      manager.edit_contact()
    elif choice == "4":
      manager.delete_contact()
    elif choice == "5":
      manager.save_contacts("contacts.txt")
    elif choice == "6":
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()