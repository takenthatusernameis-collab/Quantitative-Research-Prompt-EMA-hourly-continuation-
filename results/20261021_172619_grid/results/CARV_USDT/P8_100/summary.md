# EMA Hourly Continuation — CARV/USDT P8_100

**Symbol:** CARV/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.8255 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 1.0184 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -1.4381 |
| sortino_ratio | -0.4628 |
| max_drawdown | 0.4465 |
| cagr | -0.1939 |
| net_avg_win | 81.6980 |
| net_avg_loss | -99.4588 |
| avg_hold_time_bars | 27.5452 |
| exposure | 0.6340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
