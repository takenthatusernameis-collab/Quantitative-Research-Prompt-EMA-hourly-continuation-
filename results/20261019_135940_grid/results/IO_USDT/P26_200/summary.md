# EMA Hourly Continuation — IO/USDT P26_200

**Symbol:** IO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.6914 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9079 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -2.3751 |
| sortino_ratio | -0.6801 |
| max_drawdown | 0.5587 |
| cagr | -0.2783 |
| net_avg_win | 64.2723 |
| net_avg_loss | -85.2133 |
| avg_hold_time_bars | 29.2916 |
| exposure | 0.5545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
