# EMA Hourly Continuation — LSK/USDT P50_100

**Symbol:** LSK/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6572 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9289 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -2.6441 |
| sortino_ratio | -0.7916 |
| max_drawdown | 0.6280 |
| cagr | -0.3064 |
| net_avg_win | 54.1036 |
| net_avg_loss | -77.9302 |
| avg_hold_time_bars | 9.1689 |
| exposure | 0.1825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
