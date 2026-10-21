# EMA Hourly Continuation — ETC/USDT P8_55

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.7051 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9742 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -2.8120 |
| sortino_ratio | -1.0208 |
| max_drawdown | 0.6940 |
| cagr | -0.3728 |
| net_avg_win | 52.0532 |
| net_avg_loss | -72.0073 |
| avg_hold_time_bars | 15.8863 |
| exposure | 0.4636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
