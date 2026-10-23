# EMA Hourly Continuation — ID/USDT P34_50

**Symbol:** ID/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 810 |
| net_profit_factor | 0.3893 |
| net_win_rate | 0.4432 |
| gross_profit_factor | 0.9063 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -7.5228 |
| sortino_ratio | -3.0313 |
| max_drawdown | 0.9769 |
| cagr | -0.7753 |
| net_avg_win | 17.3425 |
| net_avg_loss | -35.4646 |
| avg_hold_time_bars | 3.4074 |
| exposure | 0.1249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
