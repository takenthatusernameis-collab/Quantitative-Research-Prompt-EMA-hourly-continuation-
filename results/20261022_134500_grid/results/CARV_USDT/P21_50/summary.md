# EMA Hourly Continuation — CARV/USDT P21_50

**Symbol:** CARV/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.5368 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.9602 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -5.5719 |
| sortino_ratio | -2.2478 |
| max_drawdown | 0.9002 |
| cagr | -0.6704 |
| net_avg_win | 32.5048 |
| net_avg_loss | -54.2587 |
| avg_hold_time_bars | 6.5822 |
| exposure | 0.2500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
