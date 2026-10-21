# EMA Hourly Continuation — GMX/USDT P8_55

**Symbol:** GMX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.6841 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.8812 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -3.3611 |
| sortino_ratio | -1.2835 |
| max_drawdown | 0.7723 |
| cagr | -0.4448 |
| net_avg_win | 49.7552 |
| net_avg_loss | -63.4700 |
| avg_hold_time_bars | 14.3218 |
| exposure | 0.4694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
