# EMA Hourly Continuation — IMX/USDT P8_50

**Symbol:** IMX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.6493 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 1.0004 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -4.5464 |
| sortino_ratio | -2.0327 |
| max_drawdown | 0.9204 |
| cagr | -0.6216 |
| net_avg_win | 34.4576 |
| net_avg_loss | -50.0133 |
| avg_hold_time_bars | 10.2559 |
| exposure | 0.4697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
