# EMA Hourly Continuation — ID/USDT P89_100

**Symbol:** ID/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.3338 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.8526 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -6.9539 |
| sortino_ratio | -2.2983 |
| max_drawdown | 0.9490 |
| cagr | -0.6917 |
| net_avg_win | 19.8824 |
| net_avg_loss | -46.9896 |
| avg_hold_time_bars | 2.9963 |
| exposure | 0.0735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
