# EMA Hourly Continuation — ZETA/USDT P12_21

**Symbol:** ZETA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1424 |
| net_profit_factor | 0.3855 |
| net_win_rate | 0.3954 |
| gross_profit_factor | 0.8292 |
| gross_win_rate | 0.4270 |
| sharpe_ratio | -12.6238 |
| sortino_ratio | -6.7709 |
| max_drawdown | 0.9998 |
| cagr | -0.9668 |
| net_avg_win | 11.1399 |
| net_avg_loss | -18.8965 |
| avg_hold_time_bars | 2.5779 |
| exposure | 0.1661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
