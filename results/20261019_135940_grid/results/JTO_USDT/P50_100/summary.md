# EMA Hourly Continuation — JTO/USDT P50_100

**Symbol:** JTO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 619 |
| net_profit_factor | 0.5210 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.8308 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -4.8971 |
| sortino_ratio | -1.7145 |
| max_drawdown | 0.8774 |
| cagr | -0.5611 |
| net_avg_win | 34.4280 |
| net_avg_loss | -53.1703 |
| avg_hold_time_bars | 5.8288 |
| exposure | 0.1640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
