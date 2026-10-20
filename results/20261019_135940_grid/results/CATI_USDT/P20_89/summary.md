# EMA Hourly Continuation — CATI/USDT P20_89

**Symbol:** CATI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.5759 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.8744 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -5.5794 |
| sortino_ratio | -2.1741 |
| max_drawdown | 0.8950 |
| cagr | -0.6469 |
| net_avg_win | 42.6468 |
| net_avg_loss | -59.3248 |
| avg_hold_time_bars | 12.4006 |
| exposure | 0.4310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
