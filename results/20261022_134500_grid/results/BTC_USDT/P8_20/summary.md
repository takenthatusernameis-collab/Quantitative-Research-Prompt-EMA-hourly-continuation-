# EMA Hourly Continuation — BTC/USDT P8_20

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1904 |
| net_profit_factor | 0.1225 |
| net_win_rate | 0.3256 |
| gross_profit_factor | 0.8208 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -19.7713 |
| sortino_ratio | -12.1406 |
| max_drawdown | 1.0000 |
| cagr | -0.9988 |
| net_avg_win | 2.2513 |
| net_avg_loss | -8.8753 |
| avg_hold_time_bars | 3.0068 |
| exposure | 0.2290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
