# EMA Hourly Continuation — ZEN/USDT P8_12

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1933 |
| net_profit_factor | 0.1402 |
| net_win_rate | 0.3663 |
| gross_profit_factor | 0.5525 |
| gross_win_rate | 0.4273 |
| sharpe_ratio | -17.5708 |
| sortino_ratio | -11.1542 |
| max_drawdown | 1.0000 |
| cagr | -0.9971 |
| net_avg_win | 2.3038 |
| net_avg_loss | -9.4948 |
| avg_hold_time_bars | 1.8024 |
| exposure | 0.1584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
