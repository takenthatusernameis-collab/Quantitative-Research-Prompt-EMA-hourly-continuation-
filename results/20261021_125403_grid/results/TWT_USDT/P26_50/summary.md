# EMA Hourly Continuation — TWT/USDT P26_50

**Symbol:** TWT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.6688 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0395 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -2.6220 |
| sortino_ratio | -0.7957 |
| max_drawdown | 0.6343 |
| cagr | -0.3035 |
| net_avg_win | 53.3082 |
| net_avg_loss | -83.0191 |
| avg_hold_time_bars | 6.3363 |
| exposure | 0.1276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
