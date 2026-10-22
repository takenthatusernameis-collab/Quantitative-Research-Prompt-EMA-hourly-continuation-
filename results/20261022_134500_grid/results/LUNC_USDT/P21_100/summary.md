# EMA Hourly Continuation — LUNC/USDT P21_100

**Symbol:** LUNC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 755 |
| net_profit_factor | 0.4166 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.7360 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -6.2282 |
| sortino_ratio | -2.4058 |
| max_drawdown | 0.9501 |
| cagr | -0.6900 |
| net_avg_win | 20.2534 |
| net_avg_loss | -38.5671 |
| avg_hold_time_bars | 10.8066 |
| exposure | 0.3709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
