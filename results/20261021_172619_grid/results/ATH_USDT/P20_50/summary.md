# EMA Hourly Continuation — ATH/USDT P20_50

**Symbol:** ATH/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.8291 |
| net_win_rate | 0.5144 |
| gross_profit_factor | 1.0602 |
| gross_win_rate | 0.5144 |
| sharpe_ratio | -1.2266 |
| sortino_ratio | -0.3723 |
| max_drawdown | 0.3759 |
| cagr | -0.1587 |
| net_avg_win | 75.4469 |
| net_avg_loss | -96.3792 |
| avg_hold_time_bars | 8.3828 |
| exposure | 0.1698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
