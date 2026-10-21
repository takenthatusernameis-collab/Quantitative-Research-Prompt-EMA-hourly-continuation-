# EMA Hourly Continuation — SNX/USDT P144_200

**Symbol:** SNX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.5749 |
| net_win_rate | 0.4311 |
| gross_profit_factor | 0.7695 |
| gross_win_rate | 0.4311 |
| sharpe_ratio | -2.6621 |
| sortino_ratio | -0.5666 |
| max_drawdown | 0.4871 |
| cagr | -0.2297 |
| net_avg_win | 67.2185 |
| net_avg_loss | -88.6114 |
| avg_hold_time_bars | 6.2889 |
| exposure | 0.0640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
