# EMA Hourly Continuation — ALT/USDT P20_26

**Symbol:** ALT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.3428 |
| net_win_rate | 0.4012 |
| gross_profit_factor | 0.8354 |
| gross_win_rate | 0.4368 |
| sharpe_ratio | -10.3714 |
| sortino_ratio | -4.6859 |
| max_drawdown | 0.9976 |
| cagr | -0.9085 |
| net_avg_win | 12.8135 |
| net_avg_loss | -25.0456 |
| avg_hold_time_bars | 3.1591 |
| exposure | 0.1453 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
