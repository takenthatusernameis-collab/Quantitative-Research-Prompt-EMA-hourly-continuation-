# EMA Hourly Continuation — BOME/USDT P8_20

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.8216 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0587 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -1.3154 |
| sortino_ratio | -0.4205 |
| max_drawdown | 0.4531 |
| cagr | -0.1768 |
| net_avg_win | 69.8260 |
| net_avg_loss | -91.0540 |
| avg_hold_time_bars | 5.4970 |
| exposure | 0.1232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
