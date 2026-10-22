# EMA Hourly Continuation — CYBER/USDT P50_89

**Symbol:** CYBER/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.8025 |
| net_win_rate | 0.5365 |
| gross_profit_factor | 1.1324 |
| gross_win_rate | 0.5365 |
| sharpe_ratio | -1.3116 |
| sortino_ratio | -0.3909 |
| max_drawdown | 0.4090 |
| cagr | -0.1643 |
| net_avg_win | 64.6588 |
| net_avg_loss | -93.2499 |
| avg_hold_time_bars | 6.7553 |
| exposure | 0.1305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
