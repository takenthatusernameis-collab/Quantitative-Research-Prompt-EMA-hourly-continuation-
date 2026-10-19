# EMA Hourly Continuation — JASMY/USDT P8_89

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.7441 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0626 |
| gross_win_rate | 0.5155 |
| sharpe_ratio | -2.7152 |
| sortino_ratio | -1.0204 |
| max_drawdown | 0.7456 |
| cagr | -0.3839 |
| net_avg_win | 57.8126 |
| net_avg_loss | -77.6901 |
| avg_hold_time_bars | 19.9266 |
| exposure | 0.6413 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
