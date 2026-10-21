# EMA Hourly Continuation — PHA/USDT P34_144

**Symbol:** PHA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.7659 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9148 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -1.5969 |
| sortino_ratio | -0.4339 |
| max_drawdown | 0.4017 |
| cagr | -0.1819 |
| net_avg_win | 74.4503 |
| net_avg_loss | -89.0240 |
| avg_hold_time_bars | 22.2940 |
| exposure | 0.3689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
