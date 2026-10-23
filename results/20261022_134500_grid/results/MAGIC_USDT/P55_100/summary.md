# EMA Hourly Continuation — MAGIC/USDT P55_100

**Symbol:** MAGIC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.5744 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9629 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -4.2752 |
| sortino_ratio | -1.4573 |
| max_drawdown | 0.8305 |
| cagr | -0.5018 |
| net_avg_win | 40.2509 |
| net_avg_loss | -64.0634 |
| avg_hold_time_bars | 5.7741 |
| exposure | 0.1522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
