from myforum.lib.db.base import BaseManager
from myforum.model import Newsletter


class LettersManager(BaseManager):
    def convert_row(self, row):
        letter = Newsletter()
        letter.newsletter_id = row[0]
        letter.newsletter_name = row[1]
        letter.from_name = row[2]
        letter.from_email = row[3]
        letter.subject = row[4]
        letter.body_text = row[5]
        letter.body_html = row[6]
        return letter

    def get_all_letters(self):
        query = '''
        SELECT * FROM letters
        '''
        return self.select_all(query)

    def get_letter(self, id):
        query = '''
        SELECT * FROM letters WHERE newsletter_id = %s
        '''
        params = (id,)
        return self.select_one(query, params)

    def add_letter(self, newsletter_name, from_name,
                   from_email, subject, body_text, body_html):
        query = '''
        INSERT INTO letters(newsletter_name, from_name,
        from_email, subject, body_text, body_html)
        VALUES(%s, %s, %s, %s, %s, %s)
        '''
        params = (newsletter_name, from_name,
                  from_email, subject, body_text, body_html)
        self.execute(query, params)

    def edit_letter(self, newsletter_id, newsletter_name, from_name,
                    from_email, subject, body_text, body_html):
        query = '''
        UPDATE letters SET newsletter_name = %s, from_name = %s,
        from_email = %s, subject = %s, body_text = %s, body_html = %s
        WHERE newsletter_id = %s
        '''
        params = (newsletter_name, from_name,
                  from_email, subject, body_text, body_html, newsletter_id,)
        self.execute(query, params)

    def delete_letter(self, newsletter_id):
        query = '''
        DELETE FROM letters WHERE newsletter_id = %s
        '''
        params = (newsletter_id,)
        self.execute(query, params)


