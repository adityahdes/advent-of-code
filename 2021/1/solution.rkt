#lang racket/base

(require racket/file)

(define nums (map string->number (file->lines "2021/1/input.txt")))

(define (part-1 n)
    (cond 
        [(null? (cdr n)) 0]
        [(< (car n) (cadr n)) (+ 1 (part-1 (cdr n)))]
        [else (part-1 (cdr n))]))

(define (part-2 n)
    (cond 
        [(null? (cdddr n)) 0]
        [(< (car n) (cadddr n)) (+ 1 (part-2 (cdr n)))]
        [else (part-2 (cdr n))]))

(part-1 nums)
(part-2 nums)