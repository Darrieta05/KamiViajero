var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('default', function() {
   gulp.watch('src/app/sass/*.sass',['styles']);
});

gulp.task('styles', function() {
    gulp.src('src/app/sass/*.sass')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('src/app/css/'));
});
