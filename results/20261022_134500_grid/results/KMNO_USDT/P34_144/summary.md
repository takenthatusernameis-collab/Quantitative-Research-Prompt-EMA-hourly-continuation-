# EMA Hourly Continuation — KMNO/USDT P34_144

**Symbol:** KMNO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.6465 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.9131 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -3.0396 |
| sortino_ratio | -0.8833 |
| max_drawdown | 0.6685 |
| cagr | -0.3478 |
| net_avg_win | 59.9614 |
| net_avg_loss | -80.9511 |
| avg_hold_time_bars | 18.7775 |
| exposure | 0.3702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
