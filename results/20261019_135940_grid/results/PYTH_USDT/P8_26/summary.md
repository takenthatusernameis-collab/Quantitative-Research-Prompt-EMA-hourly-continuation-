# EMA Hourly Continuation — PYTH/USDT P8_26

**Symbol:** PYTH/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1506 |
| net_profit_factor | 0.5461 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 1.0064 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -8.3837 |
| sortino_ratio | -4.5492 |
| max_drawdown | 0.9966 |
| cagr | -0.8955 |
| net_avg_win | 17.0332 |
| net_avg_loss | -27.3777 |
| avg_hold_time_bars | 3.8792 |
| exposure | 0.2655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
