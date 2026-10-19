# EMA Hourly Continuation — LUNC/USDT P8_34

**Symbol:** LUNC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1563 |
| net_profit_factor | 0.3248 |
| net_win_rate | 0.4088 |
| gross_profit_factor | 0.7367 |
| gross_win_rate | 0.4351 |
| sharpe_ratio | -11.6015 |
| sortino_ratio | -6.4712 |
| max_drawdown | 0.9997 |
| cagr | -0.9595 |
| net_avg_win | 7.5243 |
| net_avg_loss | -16.0225 |
| avg_hold_time_bars | 4.5099 |
| exposure | 0.3204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
