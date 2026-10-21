# EMA Hourly Continuation — MTL/USDT P89_100

**Symbol:** MTL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 208 |
| net_profit_factor | 0.5184 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.8477 |
| gross_win_rate | 0.4519 |
| sharpe_ratio | -3.0178 |
| sortino_ratio | -0.6233 |
| max_drawdown | 0.5242 |
| cagr | -0.2499 |
| net_avg_win | 59.0885 |
| net_avg_loss | -93.9781 |
| avg_hold_time_bars | 8.5769 |
| exposure | 0.0807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
