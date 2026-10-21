# EMA Hourly Continuation — SATS/USDT P21_26

**Symbol:** SATS/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 219 |
| net_profit_factor | 0.6666 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9555 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -1.8471 |
| sortino_ratio | -0.3878 |
| max_drawdown | 0.3835 |
| cagr | -0.1659 |
| net_avg_win | 68.6277 |
| net_avg_loss | -98.3576 |
| avg_hold_time_bars | 4.6712 |
| exposure | 0.0463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
