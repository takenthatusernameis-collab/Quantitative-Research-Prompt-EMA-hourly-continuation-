# EMA Hourly Continuation — GMT/USDT P89_100

**Symbol:** GMT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.2551 |
| net_win_rate | 0.3719 |
| gross_profit_factor | 0.7749 |
| gross_win_rate | 0.4172 |
| sharpe_ratio | -10.1374 |
| sortino_ratio | -3.7496 |
| max_drawdown | 0.9931 |
| cagr | -0.8622 |
| net_avg_win | 14.2899 |
| net_avg_loss | -33.1643 |
| avg_hold_time_bars | 1.9703 |
| exposure | 0.0573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
