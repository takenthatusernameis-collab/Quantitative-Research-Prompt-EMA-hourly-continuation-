# EMA Hourly Continuation — WLD/USDT P8_100

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 1.0371 |
| net_win_rate | 0.5459 |
| gross_profit_factor | 1.1879 |
| gross_win_rate | 0.5459 |
| sharpe_ratio | 0.3081 |
| sortino_ratio | 0.0933 |
| max_drawdown | 0.2765 |
| cagr | 0.0324 |
| net_avg_win | 97.8696 |
| net_avg_loss | -113.4286 |
| avg_hold_time_bars | 33.5826 |
| exposure | 0.6655 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
