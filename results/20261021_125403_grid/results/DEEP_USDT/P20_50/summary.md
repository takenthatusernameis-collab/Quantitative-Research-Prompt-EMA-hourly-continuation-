# EMA Hourly Continuation — DEEP/USDT P20_50

**Symbol:** DEEP/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.8508 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0563 |
| gross_win_rate | 0.5164 |
| sharpe_ratio | -1.1215 |
| sortino_ratio | -0.3582 |
| max_drawdown | 0.3142 |
| cagr | -0.1544 |
| net_avg_win | 80.1940 |
| net_avg_loss | -99.6255 |
| avg_hold_time_bars | 7.5617 |
| exposure | 0.1700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
