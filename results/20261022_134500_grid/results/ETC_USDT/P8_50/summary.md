# EMA Hourly Continuation — ETC/USDT P8_50

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1148 |
| net_profit_factor | 0.4877 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.9403 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -8.1197 |
| sortino_ratio | -3.8677 |
| max_drawdown | 0.9922 |
| cagr | -0.8535 |
| net_avg_win | 17.9506 |
| net_avg_loss | -31.1280 |
| avg_hold_time_bars | 8.7787 |
| exposure | 0.4581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
