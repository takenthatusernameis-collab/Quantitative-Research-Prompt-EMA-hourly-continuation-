# EMA Hourly Continuation — DYDX/USDT P8_21

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.7182 |
| net_win_rate | 0.4991 |
| gross_profit_factor | 0.9769 |
| gross_win_rate | 0.4991 |
| sharpe_ratio | -2.3439 |
| sortino_ratio | -0.8108 |
| max_drawdown | 0.6055 |
| cagr | -0.3095 |
| net_avg_win | 53.2101 |
| net_avg_loss | -73.8355 |
| avg_hold_time_bars | 5.5577 |
| exposure | 0.1468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
