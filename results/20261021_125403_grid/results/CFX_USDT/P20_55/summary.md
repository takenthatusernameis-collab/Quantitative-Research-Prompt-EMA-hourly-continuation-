# EMA Hourly Continuation — CFX/USDT P20_55

**Symbol:** CFX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.6214 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8168 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -3.3611 |
| sortino_ratio | -1.0774 |
| max_drawdown | 0.7297 |
| cagr | -0.3903 |
| net_avg_win | 50.9857 |
| net_avg_loss | -67.5861 |
| avg_hold_time_bars | 8.6272 |
| exposure | 0.1988 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
