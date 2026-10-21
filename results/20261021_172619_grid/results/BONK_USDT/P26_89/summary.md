# EMA Hourly Continuation — BONK/USDT P26_89

**Symbol:** BONK/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.7815 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9323 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -1.4733 |
| sortino_ratio | -0.4282 |
| max_drawdown | 0.4388 |
| cagr | -0.1801 |
| net_avg_win | 69.5069 |
| net_avg_loss | -84.3504 |
| avg_hold_time_bars | 16.3229 |
| exposure | 0.3079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
