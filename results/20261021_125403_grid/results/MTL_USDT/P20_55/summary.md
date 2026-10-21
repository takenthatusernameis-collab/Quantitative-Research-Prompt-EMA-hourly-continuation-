# EMA Hourly Continuation — MTL/USDT P20_55

**Symbol:** MTL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.7204 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 1.0350 |
| gross_win_rate | 0.4991 |
| sharpe_ratio | -2.8409 |
| sortino_ratio | -0.9718 |
| max_drawdown | 0.6986 |
| cagr | -0.3603 |
| net_avg_win | 61.3140 |
| net_avg_loss | -84.2248 |
| avg_hold_time_bars | 11.0876 |
| exposure | 0.2865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
