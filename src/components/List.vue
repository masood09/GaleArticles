<template>
  <header class="intro">
    <div class="intro__image"
      v-bind:style="hero_style">
    </div>

    <div class="container-fluid">
      <div class="row">
        <div class="col-xs-12">
          <div class="post">
            <h1 class="post-title">
              <a href="#">{{ randomArticle.title }}</a>
            </h1>

            <p class="post-meta">
              Posted by <a href="#">{{ randomArticle.author }}</a> on {{ randomArticle.publication_date }}
            </p>

            <div class="post-body">
              <p>
                {{{ randomArticle.body_text|truncatewords_html 100|linebreaks }}}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>

  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
        <div class="post" v-for="article in articles">
          <h2 class="post-title">
            <a href="#">
              {{ article.title }}
            </a>
          </h2>
          <p class="post-meta">
            Posted by <a href="#">{{ article.author }}</a> on {{ article.publication_date }}</p>

          <div class="post-body">
            <p>
              {{{ article.body_text|truncatewords_html 50|linebreaks }}}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        randomArticle: {
          id: '5',
          author: 'masoodahmed',
          title: 'Age nunc isti doceant, vel tu potius quis enim ista melius?',
          publication_date: 'July 15, 2013',
          hero_image: 'http://54.153.226.25:8000/media/images/demo/5.jpg',
          optional_image: 'http://54.153.226.25:8000/media/images/demo/14.jpg',
          body_text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. An quod ita callida est, ut optime possit architectari voluptates? Aut haec tibi, Torquate, sunt vituperanda aut patrocinium voluptatis repudiandum. Bonum negas esse divitias, praeposìtum esse dicis? Duo Reges: constructio interrete. Quodsi vultum tibi, si incessum fingeres, quo gravior viderere, non esses tui similis;\r\n\r\nEst autem etiam actio quaedam corporis, quae motus et status naturae congruentis tenet; Quid vero? Sed mehercule pergrata mihi oratio tua. Quid ergo attinet gloriose loqui, nisi constanter loquare? Piso, familiaris noster, et alia multa et hoc loco Stoicos irridebat: Quid enim? Primum quid tu dicis breve? Quos quidem tibi studiose et diligenter tractandos magnopere censeo. Sed quid ages tandem, si utilitas ab amicitia, ut fit saepe, defecerit?\r\n\r\nSed tamen intellego quid velit. Conclusum est enim contra Cyrenaicos satis acute, nihil ad Epicurum. At, illa, ut vobis placet, partem quandam tuetur, reliquam deserit. Semper enim ex eo, quod maximas partes continet latissimeque funditur, tota res appellatur. Beatus sibi videtur esse moriens. Iam id ipsum absurdum, maximum malum neglegi.\r\n\r\nFacillimum id quidem est, inquam. Mihi, inquam, qui te id ipsum rogavi? Tu autem negas fortem esse quemquam posse, qui dolorem malum putet. Et harum quidem rerum facilis est et expedita distinctio. Equidem etiam Epicurum, in physicis quidem, Democriteum puto. Itaque sensibus rationem adiunxit et ratione effecta sensus non reliquit.\r\n\r\nQui non moveatur et offensione turpitudinis et comprobatione honestatis? Quos quidem tibi studiose et diligenter tractandos magnopere censeo. Illa videamus, quae a te de amicitia dicta sunt. Equidem etiam Epicurum, in physicis quidem, Democriteum puto. Tum, Quintus et Pomponius cum idem se velle dixissent, Piso exorsus est. Ergo ita: non posse honeste vivi, nisi honeste vivatur?'
        },
        articles: [
          {
            id: '1',
            author: 'masoodahmed',
            title: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            publication_date: 'January 01, 2013',
            hero_image: 'http://54.153.226.25:8000/media/images/demo/1.jpg',
            optional_image: 'http://54.153.226.25:8000/media/images/demo/2.jpg',
            body_text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Tu enim ista lenius, hic Stoicorum more nos vexat. Semper enim ita adsumit aliquid, ut ea, quae prima dederit, non deserat. Quando enim Socrates, qui parens philosophiae iure dici potest, quicquam tale fecit? Quid me istud rogas? Age nunc isti doceant, vel tu potius quis enim ista melius? Apud ceteros autem philosophos, qui quaesivit aliquid, tacet; Duo Reges: constructio interrete.\r\n\r\nNam si amitti vita beata potest, beata esse non potest. Si quicquam extra virtutem habeatur in bonis. Septem autem illi non suo, sed populorum suffragio omnium nominati sunt. Tu vero, inquam, ducas licet, si sequetur; Quos quidem tibi studiose et diligenter tractandos magnopere censeo. Fortemne possumus dicere eundem illum Torquatum? Quamquam id quidem licebit iis existimare, qui legerint. Verum hoc idem saepe faciamus. Inde sermone vario sex illa a Dipylo stadia confecimus. Quis Aristidem non mortuum diligit? Quicquid porro animo cernimus, id omne oritur a sensibus; Dat enim intervalla et relaxat.\r\n\r\nQuo plebiscito decreta a senatu est consuli quaestio Cn. Illud quaero, quid ei, qui in voluptate summum bonum ponat, consentaneum sit dicere.\r\n\r\nVitiosum est enim in dividendo partem in genere numerare. Omnia peccata paria dicitis. Ergo id est convenienter naturae vivere, a natura discedere. Age, inquies, ista parva sunt. Nec vero alia sunt quaerenda contra Carneadeam illam sententiam. Dolere malum est: in crucem qui agitur, beatus esse non potest. Non est igitur voluptas bonum. Sic enim censent, oportunitatis esse beate vivere.\r\n\r\nSi quicquam extra virtutem habeatur in bonis. Quodsi ipsam honestatem undique pertectam atque absolutam. Comprehensum, quod cognitum non habet? Itaque eos id agere, ut a se dolores, morbos, debilitates repellant.'
          },
          {
            id: '2',
            author: 'masoodahmed',
            title: 'Tu enim ista lenius, hic Stoicorum more nos vexat.',
            publication_date: 'January 10, 2013',
            hero_image: 'http://54.153.226.25:8000/media/images/demo/2.jpg',
            optional_image: 'http://54.153.226.25:8000/media/images/demo/3.jpg',
            body_text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quae cum dixisset, finem ille. Et ille ridens: Video, inquit, quid agas; Duo Reges: constructio interrete. Nos cum te, M. Quae animi affectio suum cuique tribuens atque hanc, quam dico. Piso, familiaris noster, et alia multa et hoc loco Stoicos irridebat: Quid enim? Eiuro, inquit adridens, iniquum, hac quidem de re; Quid enim est a Chrysippo praetermissum in Stoicis? Non igitur bene.\r\n\r\nNe amores quidem sanctos a sapiente alienos esse arbitrantur. Ad corpus diceres pertinere-, sed ea, quae dixi, ad corpusne refers? Ait enim se, si uratur, Quam hoc suave! dicturum. Isto modo ne improbos quidem, si essent boni viri. Eadem nunc mea adversum te oratio est. Aliter enim explicari, quod quaeritur, non potest. Quem Tiberina descensio festo illo die tanto gaudio affecit, quanto L.\r\n\r\nEam tum adesse, cum dolor omnis absit; Quod ea non occurrentia fingunt, vincunt Aristonem; Qua ex cognitione facilior facta est investigatio rerum occultissimarum. Illi enim inter se dissentiunt. Haec bene dicuntur, nec ego repugno, sed inter sese ipsa pugnant. Estne, quaeso, inquam, sitienti in bibendo voluptas? Quis istud, quaeso, nesciebat?\r\n\r\nApud imperitos tum illa dicta sunt, aliquid etiam coronae datum; Ad corpus diceres pertinere-, sed ea, quae dixi, ad corpusne refers? Utrum igitur tibi litteram videor an totas paginas commovere? Summum a vobis bonum voluptas dicitur.\r\n\r\nNon enim iam stirpis bonum quaeret, sed animalis. Non laboro, inquit, de nomine. At ille pellit, qui permulcet sensum voluptate. Illud dico, ea, quae dicat, praeclare inter se cohaerere. Innumerabilia dici possunt in hanc sententiam, sed non necesse est. Qui non moveatur et offensione turpitudinis et comprobatione honestatis? Quo modo autem philosophus loquitur? Quod autem satis est, eo quicquid accessit, nimium est; Nam his libris eum malo quam reliquo ornatu villae delectari. Quia dolori non voluptas contraria est, sed doloris privatio. Et quidem iure fortasse, sed tamen non gravissimum est testimonium multitudinis.'
          }
        ]
      }
    },

    computed: {
      hero_style: function () {
        return {
          backgroundImage: 'url(\'' + this.randomArticle.hero_image + '\')'
        }
      }
    }
  }
</script>
