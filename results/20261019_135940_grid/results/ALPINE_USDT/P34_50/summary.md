# EMA Hourly Continuation — ALPINE/USDT P34_50

**Symbol:** ALPINE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 834 |
| net_profit_factor | 0.3302 |
| net_win_rate | 0.3921 |
| gross_profit_factor | 0.7370 |
| gross_win_rate | 0.4281 |
| sharpe_ratio | -9.7254 |
| sortino_ratio | -4.0261 |
| max_drawdown | 0.9938 |
| cagr | -0.8668 |
| net_avg_win | 14.9803 |
| net_avg_loss | -29.2608 |
| avg_hold_time_bars | 4.3405 |
| exposure | 0.1645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
