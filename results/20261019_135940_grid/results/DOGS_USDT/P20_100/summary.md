# EMA Hourly Continuation — DOGS/USDT P20_100

**Symbol:** DOGS/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.6803 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 0.9793 |
| gross_win_rate | 0.5092 |
| sharpe_ratio | -2.8611 |
| sortino_ratio | -1.0685 |
| max_drawdown | 0.6640 |
| cagr | -0.3957 |
| net_avg_win | 46.9305 |
| net_avg_loss | -69.6822 |
| avg_hold_time_bars | 13.3668 |
| exposure | 0.4233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
