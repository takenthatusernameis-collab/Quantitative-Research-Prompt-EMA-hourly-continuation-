# EMA Hourly Continuation — XTZ/USDT P26_100

**Symbol:** XTZ/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.6019 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 1.0098 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -4.4559 |
| sortino_ratio | -1.6123 |
| max_drawdown | 0.8640 |
| cagr | -0.5414 |
| net_avg_win | 41.0852 |
| net_avg_loss | -62.1639 |
| avg_hold_time_bars | 12.2655 |
| exposure | 0.3696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
