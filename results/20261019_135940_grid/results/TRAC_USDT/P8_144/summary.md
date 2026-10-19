# EMA Hourly Continuation — TRAC/USDT P8_144

**Symbol:** TRAC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.6675 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.9008 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -3.2499 |
| sortino_ratio | -1.0760 |
| max_drawdown | 0.7334 |
| cagr | -0.3994 |
| net_avg_win | 56.4134 |
| net_avg_loss | -72.6377 |
| avg_hold_time_bars | 27.0162 |
| exposure | 0.6828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
