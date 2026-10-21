# EMA Hourly Continuation — ZRX/USDT P8_21

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 808 |
| net_profit_factor | 0.5951 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.8862 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -5.1408 |
| sortino_ratio | -2.0913 |
| max_drawdown | 0.9108 |
| cagr | -0.6180 |
| net_avg_win | 35.9782 |
| net_avg_loss | -51.5862 |
| avg_hold_time_bars | 5.5507 |
| exposure | 0.2039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
