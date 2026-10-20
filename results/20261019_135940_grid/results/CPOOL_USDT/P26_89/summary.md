# EMA Hourly Continuation — CPOOL/USDT P26_89

**Symbol:** CPOOL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 782 |
| net_profit_factor | 0.5821 |
| net_win_rate | 0.4552 |
| gross_profit_factor | 0.8047 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -4.8070 |
| sortino_ratio | -1.8845 |
| max_drawdown | 0.9035 |
| cagr | -0.5971 |
| net_avg_win | 35.1355 |
| net_avg_loss | -50.4422 |
| avg_hold_time_bars | 6.7033 |
| exposure | 0.2383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
