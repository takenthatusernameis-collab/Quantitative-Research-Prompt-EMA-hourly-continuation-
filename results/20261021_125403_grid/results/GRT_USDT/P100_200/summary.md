# EMA Hourly Continuation — GRT/USDT P100_200

**Symbol:** GRT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.7734 |
| net_win_rate | 0.5023 |
| gross_profit_factor | 0.9896 |
| gross_win_rate | 0.5023 |
| sharpe_ratio | -1.1026 |
| sortino_ratio | -0.2324 |
| max_drawdown | 0.2679 |
| cagr | -0.1017 |
| net_avg_win | 74.2355 |
| net_avg_loss | -96.8783 |
| avg_hold_time_bars | 13.8157 |
| exposure | 0.1357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
