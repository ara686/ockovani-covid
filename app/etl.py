import sys
from datetime import datetime, date

import requests
import pandas as pd

from app import db, app
from app.models import Import, OckovaciMisto, OckovaniSpotreba, OckovaniDistribuce, OckovaniLide, OckovaniRezervace, \
    OckovaniRegistrace

from email import utils as eut


class Etl:
    """
    This class computes a lot of metrics for kraje, okresy and mista.
    """

    def fetch_all(self):
        self._import = Import(status='RUNNING')
        db.session.add(self._import)
        db.session.commit()

        try:
            self._fetch_centers()
            self._fetch_used()
            self._fetch_distributed()
            self._fetch_vaccinated()
            self._fetch_registrations()
            self._fetch_reservations()
        except Exception as e:
            app.logger.error(e)
            self._import.status = 'FAILED'
            self._import.end = datetime.now()
            db.session.commit()
            return False

        self._import.status = 'FINISHED'
        self._import.end = datetime.now()
        self._import.last_modified = self._last_modified
        db.session.commit()
        return True

    def _load_data(self):
        """
        Loads data to dataframe.
        @return:
        """

    def _compute_metric_queue_length(self, type, value):
        """
        This metric will compute queue length (reservation is false) for the specified object.
        [kraj, okres, misto]
        @return:
        """


if __name__ == '__main__':
    arguments = sys.argv[1:]
    if len(arguments) != 1:
        print('Invalid option.')
        exit(1)

    argument = arguments[0]

    fetcher = OpenDataFetcher(False)

    if argument == 'centers':
        fetcher._fetch_centers()
    elif argument == 'used':
        fetcher._fetch_used()
    elif argument == 'distributed':
        fetcher._fetch_distributed()
    elif argument == 'vaccinated':
        fetcher._fetch_vaccinated()
    elif argument == 'registrations_reservations':
        fetcher._import = Import(status='RUNNING')
        db.session.add(fetcher._import)
        db.session.commit()
        fetcher._fetch_registrations()
        fetcher._fetch_reservations()
        fetcher._import.status = 'FINISHED'
    else:
        print('Invalid option.')
        exit(1)

    db.session.commit()
