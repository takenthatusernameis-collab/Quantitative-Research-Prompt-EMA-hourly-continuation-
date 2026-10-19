# EMA Hourly Continuation — SAND/USDT P8_20

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1632 |
| net_profit_factor | 0.2580 |
| net_win_rate | 0.4185 |
| gross_profit_factor | 0.7120 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -12.8754 |
| sortino_ratio | -7.3573 |
| max_drawdown | 0.9999 |
| cagr | -0.9770 |
| net_avg_win | 5.0917 |
| net_avg_loss | -14.2011 |
| avg_hold_time_bars | 2.9638 |
| exposure | 0.2199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
