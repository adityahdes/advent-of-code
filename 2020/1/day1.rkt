#lang racket/base

(require racket/file)

(define nums (map string->number (file->lines "2020/1/input.txt")))

(for*/first ((i nums)
             (j nums)
             #:when (= 2020 (+ i j)))
             (* i j))

(for*/first ((i nums)
             (j nums)
             (k nums)
             #:when (= 2020 (+ i j k)))
             (* i j k))