import sender_stand_request
import data


# Función para cambiar el contenido del cuerpo de la solicitud (get_kit_body)
def get_kit_body(name):
    return {"name": name}


# Función para obtener un nuevo token de usuario
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    assert user_response.status_code == 201, "User creation failed"
    return user_response.json().get("authToken")


# Función para obtener los encabezados de autenticación
def get_auth_headers():
    auth_token = get_new_user_token()
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return headers


# Funciones para las aserciones (positive_assert y negative_assert_code_400)
def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 201, "Error al crear el kit"
    assert kit_body["name"] == response.json()["name"]


def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400


# Prueba 1. Crear un kit con 1 carácter en el nombre
def test_create_kit_with_one_char_name():
    kit_body = {"name": "a"}
    positive_assert(kit_body)

# Prueba 2. Crear un kit con 511 caracteres en el nombre


def test_create_kit_with_511_char_name():
    kit_body = {
        "name": """Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd
        abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc
        dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab
        cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda
        bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"""}
    positive_assert(kit_body)


# Prueba 3. Crear un kit con 0 caracteres en el nombre (nombre vacío)
def test_create_kit_with_empty_name():
    kit_body = {"name": ""}
    negative_assert_code_400(kit_body)


# Prueba 4. Crear un kit con 512 caracteres en el nombre
def test_create_kit_with_512_char_name():
    kit_body = {
        "name": """Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd
        abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc
        dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab
        cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda
        bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"""}
    negative_assert_code_400(kit_body)


# Prueba 5. Crear un kit con caracteres especiales en el nombre
def test_create_kit_with_special_characters_name():
    kit_body = {"name": "*-/$%&°#"}
    positive_assert(kit_body)


# Prueba 6. Crear un kit con espacios en el nombre
def test_create_kit_with_spaces_name():
    kit_body = {"name": " A Aaa "}
    positive_assert(kit_body)


# Prueba 7. Crear un kit con números en el nombre
def test_create_kit_with_numbers_name():
    kit_body = {"name": "123"}
    positive_assert(kit_body)


# Prueba 8. Crear un kit sin el parámetro "name"
def test_create_kit_with_missing_parameter():
    kit_body = {}
    negative_assert_code_400(kit_body)


# Prueba 9. Crear un kit con un tipo de parámetro diferente (número) en el nombre
def test_create_kit_with_different_parameter_type():
    kit_body = {"name": 123}
    negative_assert_code_400(kit_body)
