# EMA Hourly Continuation — BOME/USDT P8_100

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.5679 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.8003 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -3.8216 |
| sortino_ratio | -1.4289 |
| max_drawdown | 0.8385 |
| cagr | -0.4971 |
| net_avg_win | 32.5335 |
| net_avg_loss | -49.9240 |
| avg_hold_time_bars | 19.6858 |
| exposure | 0.6380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
