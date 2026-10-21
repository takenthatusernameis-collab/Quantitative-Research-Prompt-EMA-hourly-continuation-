# EMA Hourly Continuation — SSV/USDT P20_144

**Symbol:** SSV/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7269 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8685 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -1.9135 |
| sortino_ratio | -0.5183 |
| max_drawdown | 0.4869 |
| cagr | -0.2129 |
| net_avg_win | 70.9893 |
| net_avg_loss | -84.7004 |
| avg_hold_time_bars | 34.5902 |
| exposure | 0.5729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
