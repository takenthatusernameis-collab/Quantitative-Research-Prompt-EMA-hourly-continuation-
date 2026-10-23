# EMA Hourly Continuation — AUCTION/USDT P21_89

**Symbol:** AUCTION/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.5397 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.8365 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -5.4296 |
| sortino_ratio | -2.0113 |
| max_drawdown | 0.9145 |
| cagr | -0.6180 |
| net_avg_win | 34.7035 |
| net_avg_loss | -51.3109 |
| avg_hold_time_bars | 12.8804 |
| exposure | 0.4046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
