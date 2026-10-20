# EMA Hourly Continuation — ANKR/USDT P8_144

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.6431 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.9486 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -3.0446 |
| sortino_ratio | -0.8634 |
| max_drawdown | 0.6562 |
| cagr | -0.3463 |
| net_avg_win | 60.9472 |
| net_avg_loss | -83.1918 |
| avg_hold_time_bars | 41.7735 |
| exposure | 0.7880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
