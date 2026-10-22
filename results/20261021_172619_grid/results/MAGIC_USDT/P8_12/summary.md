# EMA Hourly Continuation — MAGIC/USDT P8_12

**Symbol:** MAGIC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.6753 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0308 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -2.9239 |
| sortino_ratio | -0.9104 |
| max_drawdown | 0.6571 |
| cagr | -0.3418 |
| net_avg_win | 57.0641 |
| net_avg_loss | -85.9488 |
| avg_hold_time_bars | 4.9362 |
| exposure | 0.1055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
