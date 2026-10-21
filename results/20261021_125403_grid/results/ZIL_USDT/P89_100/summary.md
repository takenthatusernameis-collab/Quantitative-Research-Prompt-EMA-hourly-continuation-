# EMA Hourly Continuation — ZIL/USDT P89_100

**Symbol:** ZIL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 116 |
| net_profit_factor | 0.6760 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0397 |
| gross_win_rate | 0.5086 |
| sharpe_ratio | -1.3203 |
| sortino_ratio | -0.2049 |
| max_drawdown | 0.2290 |
| cagr | -0.0891 |
| net_avg_win | 73.8607 |
| net_avg_loss | -113.1005 |
| avg_hold_time_bars | 4.8534 |
| exposure | 0.0256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
