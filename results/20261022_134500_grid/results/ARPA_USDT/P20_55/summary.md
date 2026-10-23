# EMA Hourly Continuation — ARPA/USDT P20_55

**Symbol:** ARPA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.4920 |
| net_win_rate | 0.4289 |
| gross_profit_factor | 0.8588 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -8.0032 |
| sortino_ratio | -3.6136 |
| max_drawdown | 0.9877 |
| cagr | -0.8223 |
| net_avg_win | 22.0314 |
| net_avg_loss | -33.6222 |
| avg_hold_time_bars | 5.8992 |
| exposure | 0.2701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
