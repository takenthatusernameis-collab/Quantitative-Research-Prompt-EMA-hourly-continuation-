# EMA Hourly Continuation — WEMIX/USDT P21_55

**Symbol:** WEMIX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1382 |
| net_profit_factor | 0.1957 |
| net_win_rate | 0.2829 |
| gross_profit_factor | 0.4082 |
| gross_win_rate | 0.3054 |
| sharpe_ratio | -17.1115 |
| sortino_ratio | -9.2296 |
| max_drawdown | 1.0000 |
| cagr | -0.9918 |
| net_avg_win | 6.2232 |
| net_avg_loss | -12.5461 |
| avg_hold_time_bars | 4.9255 |
| exposure | 0.3094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
