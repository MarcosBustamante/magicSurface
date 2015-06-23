module.exports = function(grunt) {

    grunt.initConfig({
        concat: {
            js: {
                src: [
                    'src/plugins/web/static/js/services/validator.js',
                    'src/plugins/web/static/js/services/*.js',
                    'src/plugins/web/static/js/api/**/*.js'
                ],
                dest: 'concat/concat.js'
            }
        },
        uglify: {
            js: {
                src: 'concat/concat.js',
                dest: 'src/plugins/web/static/magicSurface.min.js'
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');

    grunt.registerTask('default', ['concat', 'uglify']);

};
