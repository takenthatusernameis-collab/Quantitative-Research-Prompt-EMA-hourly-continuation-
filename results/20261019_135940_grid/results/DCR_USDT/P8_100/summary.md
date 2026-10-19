# EMA Hourly Continuation — DCR/USDT P8_100

**Symbol:** DCR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 753 |
| net_profit_factor | 0.5592 |
| net_win_rate | 0.4475 |
| gross_profit_factor | 0.8321 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -4.9472 |
| sortino_ratio | -1.9044 |
| max_drawdown | 0.9055 |
| cagr | -0.5976 |
| net_avg_win | 33.8539 |
| net_avg_loss | -49.0449 |
| avg_hold_time_bars | 18.9190 |
| exposure | 0.6446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
