# EMA Hourly Continuation — PHA/USDT P100_144

**Symbol:** PHA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 0.6480 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8358 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -1.9100 |
| sortino_ratio | -0.4118 |
| max_drawdown | 0.4294 |
| cagr | -0.1723 |
| net_avg_win | 65.6666 |
| net_avg_loss | -87.3332 |
| avg_hold_time_bars | 6.4541 |
| exposure | 0.0672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
