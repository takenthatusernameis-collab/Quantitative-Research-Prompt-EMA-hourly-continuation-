# EMA Hourly Continuation — CFX/USDT P55_89

**Symbol:** CFX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7063 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9518 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.9390 |
| sortino_ratio | -0.4842 |
| max_drawdown | 0.4481 |
| cagr | -0.1982 |
| net_avg_win | 69.1904 |
| net_avg_loss | -92.9381 |
| avg_hold_time_bars | 7.2862 |
| exposure | 0.1007 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
