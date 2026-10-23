# EMA Hourly Continuation — ZIL/USDT P8_12

**Symbol:** ZIL/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1798 |
| net_profit_factor | 0.1846 |
| net_win_rate | 0.3493 |
| gross_profit_factor | 0.8364 |
| gross_win_rate | 0.4255 |
| sharpe_ratio | -18.4932 |
| sortino_ratio | -11.4418 |
| max_drawdown | 1.0000 |
| cagr | -0.9979 |
| net_avg_win | 3.6044 |
| net_avg_loss | -10.4817 |
| avg_hold_time_bars | 1.9138 |
| exposure | 0.1564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
