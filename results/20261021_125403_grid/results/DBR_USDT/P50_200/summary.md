# EMA Hourly Continuation — DBR/USDT P50_200

**Symbol:** DBR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.6053 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.7997 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -2.5612 |
| sortino_ratio | -0.6035 |
| max_drawdown | 0.4754 |
| cagr | -0.2427 |
| net_avg_win | 66.2531 |
| net_avg_loss | -88.8217 |
| avg_hold_time_bars | 29.0000 |
| exposure | 0.3645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
