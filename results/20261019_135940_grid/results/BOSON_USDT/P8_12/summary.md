# EMA Hourly Continuation — BOSON/USDT P8_12

**Symbol:** BOSON/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1486 |
| net_profit_factor | 0.2721 |
| net_win_rate | 0.3775 |
| gross_profit_factor | 0.6735 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -13.7217 |
| sortino_ratio | -7.4942 |
| max_drawdown | 0.9999 |
| cagr | -0.9792 |
| net_avg_win | 6.6637 |
| net_avg_loss | -14.8516 |
| avg_hold_time_bars | 2.6682 |
| exposure | 0.1802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
