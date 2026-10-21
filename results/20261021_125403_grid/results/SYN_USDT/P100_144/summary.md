# EMA Hourly Continuation — SYN/USDT P100_144

**Symbol:** SYN/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.7657 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.0045 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -1.2949 |
| sortino_ratio | -0.2984 |
| max_drawdown | 0.3288 |
| cagr | -0.1285 |
| net_avg_win | 73.4408 |
| net_avg_loss | -97.4082 |
| avg_hold_time_bars | 7.7907 |
| exposure | 0.0914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
