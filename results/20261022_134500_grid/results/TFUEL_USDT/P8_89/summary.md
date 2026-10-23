# EMA Hourly Continuation — TFUEL/USDT P8_89

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1004 |
| net_profit_factor | 0.5659 |
| net_win_rate | 0.4343 |
| gross_profit_factor | 0.8773 |
| gross_win_rate | 0.4492 |
| sharpe_ratio | -6.7482 |
| sortino_ratio | -2.9972 |
| max_drawdown | 0.9745 |
| cagr | -0.7639 |
| net_avg_win | 29.1145 |
| net_avg_loss | -39.4927 |
| avg_hold_time_bars | 12.4761 |
| exposure | 0.5668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
