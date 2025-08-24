
# 1.3 The Kleio Notation for Historical Souces

_Kleio_ files are text files with a special notation designed to the transcription of historical sources. The notation was created by Manfred Thaller, as part of the _Kleio historical database system_ (http://web.archive.org/web/20130603204750/http://www.hki.uni-koeln.de/kleio/old.website/).

Although Thaller's Kleio database system is no longer publicly available, the notation developed for historical source transcription proved very powerful, providing a concise way for the transcription of complex historical documents.

Timelink implements a subset of the Kleio notation designed for its specific data models. _Timelink_ provides a set of data models designed for handling person-oriented information collected in historical documents.

  This is how a (portuguese) baptism looks like in _Timelink_ Kleio notation:

      bap$b1685.15/4/9/1685/?/igreja de s. tiago/obs=data sic

         n$mariana/f/id=b1685.15-per1

            pai$manuel gomes/m/id=b1685.15-per1-per2

            mae$isabel da gante/id=b1685.15-per1-per3

            pad$manuel duarte/m/id=b1685.15.4
               ls$profissao/padre
               ls$titulo/licenciado
               ls$titulo/frei

            mad$mariana colaco/f/id=b1685.15-per4
               rel$parentesco/irma/manuel duarte/b1685.15.4

In this example we have the registration of an "act", introduced with "bap\$" and then a certain number of "actors" introduced with words such as "celebrante", "n\$", "pn\$", "mn\$", etc...

Some of the actors have extra information  appended in lines started with "ls\$". "ls"  stands for "life-story"
and allows the registration of a time varying attribute. 

---

[[Timelink - documentation]]
