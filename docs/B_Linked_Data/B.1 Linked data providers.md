
Linked data providers are external sites to which timelink can link.

Linking to external involves three steps.

### 1. Define linked data patterns

Linked data patterns are declared in each kleio file, bellow the initial `kleio$` group.

	kleio$
		link$wikidata/"https://www.wikidata.org/wiki/$1"

The `link$` group associates a shortcut `wikidata` with a URL pattern:  `https://www.wikidata.org/wiki/$1`

### 2. Anotate sources with linked data shortcuts

In source transcriptions specific linked data is registered by including in comments sequences such as `wikidata:Q919362`. 

	n$António de Abreu/id=deh-antonio-de-abreu
		ls$jesuita-entrada/Goa, Índia# @wikidata:Q1171/15791200
		ls$jesuita-votos-local/Negapattinam, Índia%Negapatami (Négapatam)# @wikidata:Q695585/16040106
		ls$morte/Changchow, China#no rio, a caminho do Japão @wikidata:Q57970/16110000

This generated extra attributes with the full URL

	n$António de Abreu/m/id=deh-antonio-de-abreu
	  ls$jesuita-entrada@wikidata/"https://www.wikidata.org/wiki/Q1171"%Goa, Índia/15791200
	  ls$jesuita-entrada/Goa, Índia#@wikidata:Q1171/15791200
	  ls$jesuita-votos-local@wikidata/"https://www.wikidata.org/wiki/Q695585"%Negapattinam, Índia/16040106
	  ls$jesuita-votos-local/Negapattinam, Índia#@wikidata:Q695585%Negapatami (Négapatam)/16040106
	  ls$morte@wikidata/"https://www.wikidata.org/wiki/Q57970"%Changchow, China/16110000
	  ls$morte/Changchow, China#no rio, a caminho do Japão @wikidata:Q57970/16110000

		   
Additional behaviour can be provided through plug-ins, such as fetching linked data properties (TBD).

### Usefull linked data links

#### Timelink (MHK) legacy sites

	link$uc-china/"https://timelink.uc.pt/mhk/china/id/$1"

#### Wikidata

	link$wikidata/"https://www.wikidata.org/wiki/$1"

#### Geonames

	link$geonames/"https://www.geonames.org/$1"

#### Portuguese National Library

##### Biblioteca Nacional Digital

    link$bnpd/"https://purl.pt/$1"/obs="Biblioteca Nacional de Portugal - Digital"

##### Biblioteca Nacional bibliographic record

    link$bnp/"http://id.bnportugal.gov.pt/bib/catbnp/$1"/obs="Biblioteca Nacional de Portugal 

To obtain the id check in a record display  click on "Link persistente do registo" 

You will get something like: http://id.bnportugal.gov.pt/bib/catbnp/245305

245305 is the id to use and the annotation in a source would be `@bnp:245305` 

#### Portuguese online archives system (digiarq)

##### Arquivo distrital de Viseu

    link$digiarq.advis/"https://digitarq.advis.arquivos.pt/details?id=$1"