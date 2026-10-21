# EMA Hourly Continuation — SNX/USDT P26_200

**Symbol:** SNX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.8283 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9929 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.1007 |
| sortino_ratio | -0.2881 |
| max_drawdown | 0.3324 |
| cagr | -0.1255 |
| net_avg_win | 82.9069 |
| net_avg_loss | -98.9134 |
| avg_hold_time_bars | 34.6250 |
| exposure | 0.5264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
