# EMA Hourly Continuation — ORDI/USDT P21_50

**Symbol:** ORDI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7224 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.9292 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -2.5686 |
| sortino_ratio | -0.7991 |
| max_drawdown | 0.6163 |
| cagr | -0.3073 |
| net_avg_win | 69.9497 |
| net_avg_loss | -86.0756 |
| avg_hold_time_bars | 7.0567 |
| exposure | 0.1527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
