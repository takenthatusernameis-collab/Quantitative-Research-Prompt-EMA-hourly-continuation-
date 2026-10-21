# EMA Hourly Continuation — MEW/USDT P8_55

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.7985 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 0.9833 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -1.9130 |
| sortino_ratio | -0.6933 |
| max_drawdown | 0.5622 |
| cagr | -0.2745 |
| net_avg_win | 68.7292 |
| net_avg_loss | -84.7435 |
| avg_hold_time_bars | 15.9673 |
| exposure | 0.4667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
