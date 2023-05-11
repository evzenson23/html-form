# Creation of form 

class Form:
    def __init__(self, method='POST'):
        self.method = method
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        form_start_tag = f'<form method="{self.method}">'
        form_end_tag = '</form>'
        elements_html = "\n".join([element.render() for element in self.elements])

        return form_start_tag + '\n' + elements_html + '\n' + form_end_tag

# Creation of input

class Input:
    def __init__(self, name, input_type):
        self.name = name
        self.input_type = input_type

    def render(self):
        input_tag = f'<b>{self.name}:</b> <input type="{self.input_type}" name="{self.name}">'

        return input_tag


# Creation of select

class Select:
    def __init__(self, name, options):
        self.name = name
        self.options = options

    def render(self):
        option_tags = ''.join([f'<option value="{value}">{label}</option>' for value, label in self.options])
        select_tag = f'<select name="{self.name}">{option_tags}</select>'

        return select_tag


# Creation of image

class Image:
    def __init__(self, src, alt=None):
        self.src = src
        self.alt = alt

    def render(self):
        img_tag = f'<img src="{self.src}"'
        if self.alt:
            img_tag += f' alt="{self.alt}"'
        img_tag += '>'

        return img_tag


# Creation of anchor

class Anchor:
    def __init__(self, href, text):
        self.href = href
        self.text = text

    def render(self):
        a_tag = f'<a href="{self.href}">{self.text}</a>'

        return a_tag


# Creation of div

class Div:
    def __init__(self, child):
        
        self.child = child


    def render(self):
        child_html = self.child.render()
        div_tag = f'<div>{child_html}</div>'

        return div_tag


# Creation of instance of class Form

form = Form()

# Creation of each html element as a child of div element  
username_input = Div(Input('username', 'text'))
email_input = Div(Input('email', 'email'))
password_input = Div(Input('password', 'password'))
gender_select = Div(Select('gender', [('M', 'Male'), ('F', 'Female')]))
logo = Div(Image("https://www.w3schools.com/images/w3schools_green.jpg", 'Logo'))
submit_button = Div(Input('submit', 'submit'))
anchor = Div(Anchor("https://www.w3schools.com", 'Homepage'))


# Adding each element into the form 

form.add_element(username_input)
form.add_element(email_input)
form.add_element(password_input)
form.add_element(gender_select)
form.add_element(logo)
form.add_element(submit_button)
form.add_element(anchor)

# Generating HTML code for the form
html = form.render()
print(html)


