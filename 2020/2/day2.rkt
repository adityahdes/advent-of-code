#lang racket

(require megaparsack
        megaparsack/text
        data/monad
        data/applicative
        data/either)

(define constraints/p
    (do (num1 <- integer/p)
        (char/p #\-)
        (num2 <- integer/p)
        space/p
        (letter <- letter/p)
        (char/p #\:)
        space/p
        (password-chars <- (many/p letter/p))
        eof/p
        (pure (list num1 num2 letter password-chars))))

(define (valid? line)
    