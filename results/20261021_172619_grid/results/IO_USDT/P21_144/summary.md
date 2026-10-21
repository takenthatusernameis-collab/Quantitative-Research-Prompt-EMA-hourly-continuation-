# EMA Hourly Continuation — IO/USDT P21_144

**Symbol:** IO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.8134 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9458 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -1.3126 |
| sortino_ratio | -0.3712 |
| max_drawdown | 0.3580 |
| cagr | -0.1586 |
| net_avg_win | 81.4450 |
| net_avg_loss | -94.3351 |
| avg_hold_time_bars | 29.4092 |
| exposure | 0.5254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
