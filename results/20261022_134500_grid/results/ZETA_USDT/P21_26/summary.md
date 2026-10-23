# EMA Hourly Continuation — ZETA/USDT P21_26

**Symbol:** ZETA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1199 |
| net_profit_factor | 0.2562 |
| net_win_rate | 0.3653 |
| gross_profit_factor | 0.7538 |
| gross_win_rate | 0.4262 |
| sharpe_ratio | -13.7006 |
| sortino_ratio | -6.8440 |
| max_drawdown | 0.9999 |
| cagr | -0.9722 |
| net_avg_win | 7.8611 |
| net_avg_loss | -17.6636 |
| avg_hold_time_bars | 2.0417 |
| exposure | 0.1108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
