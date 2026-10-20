# EMA Hourly Continuation — MINA/USDT P55_89

**Symbol:** MINA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.4942 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.9143 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -6.0172 |
| sortino_ratio | -2.2296 |
| max_drawdown | 0.9387 |
| cagr | -0.6628 |
| net_avg_win | 29.4649 |
| net_avg_loss | -49.5491 |
| avg_hold_time_bars | 4.3236 |
| exposure | 0.1342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
