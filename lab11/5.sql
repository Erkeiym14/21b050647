CREATE OR REPLACE PROCEDURE delete_user_by_name_or_phone(
    user_name VARCHAR(255),
    user_phone VARCHAR(255)
) AS $$
BEGIN
    IF user_name IS NOT NULL THEN
        DELETE FROM phonebook WHERE first_name = user_name OR last_name = user_name;
    END IF;

    IF user_phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = user_phone;
    END IF;
END;
$$ LANGUAGE plpgsql;
