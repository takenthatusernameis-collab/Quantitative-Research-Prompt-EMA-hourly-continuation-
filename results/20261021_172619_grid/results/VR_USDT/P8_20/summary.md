# EMA Hourly Continuation — VR/USDT P8_20

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.6094 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.8600 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -3.4644 |
| sortino_ratio | -0.9377 |
| max_drawdown | 0.6723 |
| cagr | -0.3587 |
| net_avg_win | 64.7505 |
| net_avg_loss | -83.9656 |
| avg_hold_time_bars | 8.7902 |
| exposure | 0.1466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
