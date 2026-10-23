# EMA Hourly Continuation — ANYONE/USDT P34_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.7059 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 0.8626 |
| gross_win_rate | 0.4671 |
| sharpe_ratio | -1.9099 |
| sortino_ratio | -0.4839 |
| max_drawdown | 0.4462 |
| cagr | -0.2020 |
| net_avg_win | 71.0054 |
| net_avg_loss | -88.1795 |
| avg_hold_time_bars | 38.1730 |
| exposure | 0.5575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
