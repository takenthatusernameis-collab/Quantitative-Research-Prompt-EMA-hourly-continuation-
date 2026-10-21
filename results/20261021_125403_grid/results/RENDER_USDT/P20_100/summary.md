# EMA Hourly Continuation — RENDER/USDT P20_100

**Symbol:** RENDER/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.8302 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 1.0077 |
| gross_win_rate | 0.5048 |
| sharpe_ratio | -1.2659 |
| sortino_ratio | -0.3993 |
| max_drawdown | 0.3990 |
| cagr | -0.1701 |
| net_avg_win | 76.9014 |
| net_avg_loss | -94.4202 |
| avg_hold_time_bars | 17.2201 |
| exposure | 0.3799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
