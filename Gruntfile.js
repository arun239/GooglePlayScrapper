module.exports = function(grunt) {
  grunt.initConfig({
  pkg: grunt.file.readJSON('package.json'),
  watch: {
    options: {
      livereload: true,
    },
    css: {
      files: ['css/**/*.css'],
    },
    js: {
      files: ['js/**/*.js'],
    },
    html: {
      files: ['*.html'],
    }
  },
  connect: {
    server: {
      options: {
        port: 9000,
        base: '.',
        hostname: 'localhost',
        protocol: 'http',
        livereload: true,
        open: true,
      }
    }
  },
});
grunt.loadNpmTasks('grunt-contrib-watch');
grunt.loadNpmTasks('grunt-contrib-connect');
grunt.registerTask('server', ['connect','watch']);
};