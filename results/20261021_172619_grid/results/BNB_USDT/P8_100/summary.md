# EMA Hourly Continuation — BNB/USDT P8_100

**Symbol:** BNB/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.6732 |
| net_win_rate | 0.5055 |
| gross_profit_factor | 1.0049 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -2.5993 |
| sortino_ratio | -0.7943 |
| max_drawdown | 0.6110 |
| cagr | -0.3056 |
| net_avg_win | 53.7200 |
| net_avg_loss | -81.5756 |
| avg_hold_time_bars | 30.8703 |
| exposure | 0.6385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
