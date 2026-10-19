# EMA Hourly Continuation — SAND/USDT P21_26

**Symbol:** SAND/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1150 |
| net_profit_factor | 0.1842 |
| net_win_rate | 0.3313 |
| gross_profit_factor | 0.7526 |
| gross_win_rate | 0.3974 |
| sharpe_ratio | -15.6459 |
| sortino_ratio | -7.8502 |
| max_drawdown | 1.0000 |
| cagr | -0.9861 |
| net_avg_win | 5.9260 |
| net_avg_loss | -15.9396 |
| avg_hold_time_bars | 1.7443 |
| exposure | 0.0912 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
