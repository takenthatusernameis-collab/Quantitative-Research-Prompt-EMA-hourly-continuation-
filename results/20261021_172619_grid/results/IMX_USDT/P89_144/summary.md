# EMA Hourly Continuation — IMX/USDT P89_144

**Symbol:** IMX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7252 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 0.9483 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -1.5946 |
| sortino_ratio | -0.3895 |
| max_drawdown | 0.3951 |
| cagr | -0.1633 |
| net_avg_win | 66.3967 |
| net_avg_loss | -89.0781 |
| avg_hold_time_bars | 7.5137 |
| exposure | 0.0993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
