# EMA Hourly Continuation — AEVO/USDT P20_26

**Symbol:** AEVO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.5596 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.7995 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -3.2210 |
| sortino_ratio | -0.7785 |
| max_drawdown | 0.6074 |
| cagr | -0.3011 |
| net_avg_win | 59.5409 |
| net_avg_loss | -83.9239 |
| avg_hold_time_bars | 4.6667 |
| exposure | 0.0608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
