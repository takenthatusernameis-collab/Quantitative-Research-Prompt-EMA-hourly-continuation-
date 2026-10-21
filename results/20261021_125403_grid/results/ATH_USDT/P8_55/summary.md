# EMA Hourly Continuation — ATH/USDT P8_55

**Symbol:** ATH/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.8908 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.0914 |
| gross_win_rate | 0.5244 |
| sharpe_ratio | -0.8276 |
| sortino_ratio | -0.3051 |
| max_drawdown | 0.3515 |
| cagr | -0.1364 |
| net_avg_win | 73.9916 |
| net_avg_loss | -91.5921 |
| avg_hold_time_bars | 15.2215 |
| exposure | 0.4530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
