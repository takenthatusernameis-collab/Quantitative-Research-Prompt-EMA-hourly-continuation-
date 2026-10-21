# EMA Hourly Continuation — SUSHI/USDT P26_55

**Symbol:** SUSHI/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.6874 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.9200 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -2.9079 |
| sortino_ratio | -0.9092 |
| max_drawdown | 0.6627 |
| cagr | -0.3407 |
| net_avg_win | 63.2655 |
| net_avg_loss | -81.2545 |
| avg_hold_time_bars | 6.7033 |
| exposure | 0.1462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
