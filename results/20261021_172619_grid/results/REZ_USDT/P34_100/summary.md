# EMA Hourly Continuation — REZ/USDT P34_100

**Symbol:** REZ/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.9445 |
| net_win_rate | 0.5371 |
| gross_profit_factor | 1.1475 |
| gross_win_rate | 0.5371 |
| sharpe_ratio | -0.3217 |
| sortino_ratio | -0.0988 |
| max_drawdown | 0.2784 |
| cagr | -0.0509 |
| net_avg_win | 86.3000 |
| net_avg_loss | -106.0118 |
| avg_hold_time_bars | 14.2854 |
| exposure | 0.2933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
