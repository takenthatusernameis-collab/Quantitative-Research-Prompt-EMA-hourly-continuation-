# EMA Hourly Continuation — RUNE/USDT P12_50

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 587 |
| net_profit_factor | 0.7516 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9905 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -2.4075 |
| sortino_ratio | -0.8351 |
| max_drawdown | 0.6401 |
| cagr | -0.3174 |
| net_avg_win | 64.3608 |
| net_avg_loss | -83.6086 |
| avg_hold_time_bars | 12.7274 |
| exposure | 0.3396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
