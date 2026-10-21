# EMA Hourly Continuation — BSV/USDT P50_55

**Symbol:** BSV/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 152 |
| net_profit_factor | 0.4563 |
| net_win_rate | 0.4145 |
| gross_profit_factor | 0.7072 |
| gross_win_rate | 0.4145 |
| sharpe_ratio | -2.9151 |
| sortino_ratio | -0.5148 |
| max_drawdown | 0.4486 |
| cagr | -0.2110 |
| net_avg_win | 59.7643 |
| net_avg_loss | -92.7102 |
| avg_hold_time_bars | 5.2039 |
| exposure | 0.0360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
