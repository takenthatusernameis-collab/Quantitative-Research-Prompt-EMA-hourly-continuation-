# EMA Hourly Continuation — AR/USDT P8_50

**Symbol:** AR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1003 |
| net_profit_factor | 0.5552 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8389 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -5.4960 |
| sortino_ratio | -2.4462 |
| max_drawdown | 0.9501 |
| cagr | -0.6947 |
| net_avg_win | 25.5292 |
| net_avg_loss | -39.5868 |
| avg_hold_time_bars | 11.2712 |
| exposure | 0.5139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
