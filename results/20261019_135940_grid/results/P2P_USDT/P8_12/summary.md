# EMA Hourly Continuation — P2P/USDT P8_12

**Symbol:** P2P/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1794 |
| net_profit_factor | 0.1826 |
| net_win_rate | 0.2453 |
| gross_profit_factor | 0.4452 |
| gross_win_rate | 0.2592 |
| sharpe_ratio | -20.7876 |
| sortino_ratio | -12.6796 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 5.0784 |
| net_avg_loss | -9.0358 |
| avg_hold_time_bars | 2.5396 |
| exposure | 0.2071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
