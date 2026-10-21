# EMA Hourly Continuation — ATOM/USDT P20_21

**Symbol:** ATOM/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 101 |
| net_profit_factor | 0.5700 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.8219 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -1.8253 |
| sortino_ratio | -0.2624 |
| max_drawdown | 0.3171 |
| cagr | -0.1143 |
| net_avg_win | 77.3708 |
| net_avg_loss | -109.0779 |
| avg_hold_time_bars | 5.4356 |
| exposure | 0.0250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
