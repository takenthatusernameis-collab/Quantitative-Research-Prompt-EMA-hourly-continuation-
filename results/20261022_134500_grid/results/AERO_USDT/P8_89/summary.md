# EMA Hourly Continuation — AERO/USDT P8_89

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.8323 |
| net_win_rate | 0.5190 |
| gross_profit_factor | 1.0983 |
| gross_win_rate | 0.5235 |
| sharpe_ratio | -1.5975 |
| sortino_ratio | -0.5827 |
| max_drawdown | 0.5275 |
| cagr | -0.2431 |
| net_avg_win | 73.0131 |
| net_avg_loss | -94.6419 |
| avg_hold_time_bars | 21.2337 |
| exposure | 0.6360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
