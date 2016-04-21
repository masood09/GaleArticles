$(document).ready(function(){
    //Navigation Menu Slider
    $('#nav-expander').on('click',function(e){
        e.preventDefault();
        $('body').toggleClass('nav-expanded');
    });

    $('#nav-close').on('click',function(e){
        e.preventDefault();
        $('body').removeClass('nav-expanded');
    });

    $('.slick__carousel').slick();
});

Vue.config.devtools = false;
Vue.config.delimiters = ['${', '}'];
Vue.config.unsafeDelimiters = ['{!!', '!!}'];

article__detail = {
    init: function() {
        new Vue({
            el: '#vue__container',

            data: {
                article: [],
            },

            ready: function() {
                this.$http({url: jQuery('#api__article_detail_url').val(), method: 'GET'}).then(function (response) {
                    this.$set('article', response.data)
                }, function (response) {
                    console.log(response);
                });
            },

            computed: {
                body_text_linebreaks: function () {
                    return this.article.body_text.replace(/(?:\r\n|\r|\n)/g, '<br>');
                },

                hero_style: function() {
                    return {
                        backgroundImage: 'url(\'' + this.article.hero_image + '\')'
                    };
                }
            }
        });
    }
};
