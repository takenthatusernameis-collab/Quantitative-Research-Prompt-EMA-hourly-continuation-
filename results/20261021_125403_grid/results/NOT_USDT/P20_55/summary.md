# EMA Hourly Continuation — NOT/USDT P20_55

**Symbol:** NOT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.8590 |
| net_win_rate | 0.5256 |
| gross_profit_factor | 1.0901 |
| gross_win_rate | 0.5256 |
| sharpe_ratio | -0.9890 |
| sortino_ratio | -0.3207 |
| max_drawdown | 0.3723 |
| cagr | -0.1397 |
| net_avg_win | 72.6024 |
| net_avg_loss | -93.6234 |
| avg_hold_time_bars | 7.9387 |
| exposure | 0.1824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
