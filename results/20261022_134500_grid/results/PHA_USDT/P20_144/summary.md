# EMA Hourly Continuation — PHA/USDT P20_144

**Symbol:** PHA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.6349 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.8905 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -3.3201 |
| sortino_ratio | -1.0835 |
| max_drawdown | 0.7377 |
| cagr | -0.4053 |
| net_avg_win | 50.0969 |
| net_avg_loss | -69.0749 |
| avg_hold_time_bars | 21.5000 |
| exposure | 0.5297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
