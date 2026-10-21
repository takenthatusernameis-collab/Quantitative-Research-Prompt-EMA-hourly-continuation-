# EMA Hourly Continuation — AKT/USDT P8_21

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.6452 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8502 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -2.9765 |
| sortino_ratio | -0.9478 |
| max_drawdown | 0.7040 |
| cagr | -0.3527 |
| net_avg_win | 52.3113 |
| net_avg_loss | -69.8845 |
| avg_hold_time_bars | 5.7395 |
| exposure | 0.1302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
