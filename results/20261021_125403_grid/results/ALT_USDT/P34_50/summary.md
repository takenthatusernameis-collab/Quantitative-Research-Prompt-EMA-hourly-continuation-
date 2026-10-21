# EMA Hourly Continuation — ALT/USDT P34_50

**Symbol:** ALT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6803 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9525 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -2.4273 |
| sortino_ratio | -0.7017 |
| max_drawdown | 0.5668 |
| cagr | -0.2745 |
| net_avg_win | 59.1553 |
| net_avg_loss | -83.1953 |
| avg_hold_time_bars | 6.2260 |
| exposure | 0.1152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
