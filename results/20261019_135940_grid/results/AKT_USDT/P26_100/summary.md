# EMA Hourly Continuation — AKT/USDT P26_100

**Symbol:** AKT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.6039 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.9089 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -4.1358 |
| sortino_ratio | -1.5193 |
| max_drawdown | 0.8464 |
| cagr | -0.5207 |
| net_avg_win | 40.1270 |
| net_avg_loss | -57.9389 |
| avg_hold_time_bars | 10.2183 |
| exposure | 0.3191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
