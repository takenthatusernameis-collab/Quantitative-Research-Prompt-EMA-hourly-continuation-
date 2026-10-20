# EMA Hourly Continuation — ID/USDT P8_50

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 979 |
| net_profit_factor | 0.6585 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 1.1051 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -4.5337 |
| sortino_ratio | -1.9861 |
| max_drawdown | 0.9118 |
| cagr | -0.6153 |
| net_avg_win | 36.5657 |
| net_avg_loss | -53.4133 |
| avg_hold_time_bars | 10.6088 |
| exposure | 0.4700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
