# EMA Hourly Continuation — ZRX/USDT P8_50

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1071 |
| net_profit_factor | 0.5054 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8221 |
| gross_win_rate | 0.4585 |
| sharpe_ratio | -6.7379 |
| sortino_ratio | -3.0835 |
| max_drawdown | 0.9774 |
| cagr | -0.7769 |
| net_avg_win | 20.7061 |
| net_avg_loss | -33.5301 |
| avg_hold_time_bars | 10.0775 |
| exposure | 0.4906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
