# EMA Hourly Continuation — ROSE/USDT P50_55

**Symbol:** ROSE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 858 |
| net_profit_factor | 0.2724 |
| net_win_rate | 0.3671 |
| gross_profit_factor | 0.7913 |
| gross_win_rate | 0.4126 |
| sharpe_ratio | -11.9197 |
| sortino_ratio | -5.0738 |
| max_drawdown | 0.9989 |
| cagr | -0.9341 |
| net_avg_win | 11.8713 |
| net_avg_loss | -25.2830 |
| avg_hold_time_bars | 1.9918 |
| exposure | 0.0777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
