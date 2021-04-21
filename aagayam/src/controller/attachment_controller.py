from sqlalchemy.orm import Session
from src import models, schemas

def attachments(db: Session, originalName,modifiedName, url):
    newAttachment = models.Attachment(original_name= originalName, given_name=modifiedName, attachment_url=url)
    db.add(newAttachment)
    db.commit()
    db.refresh(newAttachment)
    return newAttachment


def get_attachments_by_ids(db: Session, attIDs):
    print(attIDs)
    attachmentsData = db.query(models.Attachment).filter(models.Attachment.id.in_(attIDs)).all()

    return attachmentsData