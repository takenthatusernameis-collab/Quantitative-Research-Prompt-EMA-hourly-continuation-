# EMA Hourly Continuation — STRK/USDT P21_55

**Symbol:** STRK/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7662 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9776 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -1.7685 |
| sortino_ratio | -0.5588 |
| max_drawdown | 0.4797 |
| cagr | -0.2266 |
| net_avg_win | 64.3851 |
| net_avg_loss | -83.3446 |
| avg_hold_time_bars | 7.7901 |
| exposure | 0.1721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
