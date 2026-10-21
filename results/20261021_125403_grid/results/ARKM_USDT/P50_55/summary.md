# EMA Hourly Continuation — ARKM/USDT P50_55

**Symbol:** ARKM/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 104 |
| net_profit_factor | 0.8516 |
| net_win_rate | 0.5385 |
| gross_profit_factor | 1.1650 |
| gross_win_rate | 0.5385 |
| sharpe_ratio | -0.5116 |
| sortino_ratio | -0.0755 |
| max_drawdown | 0.1810 |
| cagr | -0.0346 |
| net_avg_win | 86.6876 |
| net_avg_loss | -118.7591 |
| avg_hold_time_bars | 5.4519 |
| exposure | 0.0258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
