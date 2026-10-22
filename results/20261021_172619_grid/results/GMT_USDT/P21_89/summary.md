# EMA Hourly Continuation — GMT/USDT P21_89

**Symbol:** GMT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.6804 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8588 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -2.8396 |
| sortino_ratio | -0.8997 |
| max_drawdown | 0.6721 |
| cagr | -0.3393 |
| net_avg_win | 60.6764 |
| net_avg_loss | -74.9697 |
| avg_hold_time_bars | 15.6539 |
| exposure | 0.3536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
