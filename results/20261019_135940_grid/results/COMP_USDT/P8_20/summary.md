# EMA Hourly Continuation — COMP/USDT P8_20

**Symbol:** COMP/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1727 |
| net_profit_factor | 0.2270 |
| net_win_rate | 0.4047 |
| gross_profit_factor | 0.6131 |
| gross_win_rate | 0.4372 |
| sharpe_ratio | -13.9351 |
| sortino_ratio | -8.2224 |
| max_drawdown | 1.0000 |
| cagr | -0.9849 |
| net_avg_win | 4.2010 |
| net_avg_loss | -12.5839 |
| avg_hold_time_bars | 2.9710 |
| exposure | 0.2332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
