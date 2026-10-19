# EMA Hourly Continuation — BTT/USDT P26_89

**Symbol:** BTT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.3604 |
| net_win_rate | 0.3529 |
| gross_profit_factor | 0.7599 |
| gross_win_rate | 0.3982 |
| sharpe_ratio | -10.1939 |
| sortino_ratio | -3.8128 |
| max_drawdown | 0.9933 |
| cagr | -0.8637 |
| net_avg_win | 23.9173 |
| net_avg_loss | -36.1995 |
| avg_hold_time_bars | 12.1629 |
| exposure | 0.3665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
