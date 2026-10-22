# EMA Hourly Continuation — CELR/USDT P26_55

**Symbol:** CELR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.6891 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.9458 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -2.9677 |
| sortino_ratio | -0.9816 |
| max_drawdown | 0.7015 |
| cagr | -0.3618 |
| net_avg_win | 58.4534 |
| net_avg_loss | -77.8626 |
| avg_hold_time_bars | 7.9870 |
| exposure | 0.1941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
