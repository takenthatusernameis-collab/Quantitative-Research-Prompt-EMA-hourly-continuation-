# EMA Hourly Continuation — JASMY/USDT P8_55

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.8098 |
| net_win_rate | 0.4993 |
| gross_profit_factor | 0.9889 |
| gross_win_rate | 0.4993 |
| sharpe_ratio | -1.7738 |
| sortino_ratio | -0.6704 |
| max_drawdown | 0.6063 |
| cagr | -0.2672 |
| net_avg_win | 66.3025 |
| net_avg_loss | -81.6395 |
| avg_hold_time_bars | 12.7231 |
| exposure | 0.4031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
