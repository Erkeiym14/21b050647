CREATE OR REPLACE PROCEDURE insert_multiple_users(
    user_data_list VARCHAR(255)[][],
    OUT invalid_data VARCHAR(255)[][]
) AS $$
DECLARE
    user_data VARCHAR(255)[];
BEGIN
    invalid_data := ARRAY[]::VARCHAR(255)[];
    FOREACH user_data IN ARRAY user_data_list
    LOOP
        -- Проверка корректности номера телефона
        IF LENGTH(user_data[1]) <> 10 THEN
            invalid_data := invalid_data || user_data;
        ELSE
            INSERT INTO phonebook(first_name, last_name, phone)
            VALUES(user_data[0], user_data[1], user_data[2]);
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
