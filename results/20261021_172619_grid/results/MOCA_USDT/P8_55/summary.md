# EMA Hourly Continuation — MOCA/USDT P8_55

**Symbol:** MOCA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.7439 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9487 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -2.5121 |
| sortino_ratio | -0.9301 |
| max_drawdown | 0.6666 |
| cagr | -0.3475 |
| net_avg_win | 60.6045 |
| net_avg_loss | -77.8118 |
| avg_hold_time_bars | 15.1803 |
| exposure | 0.4642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
