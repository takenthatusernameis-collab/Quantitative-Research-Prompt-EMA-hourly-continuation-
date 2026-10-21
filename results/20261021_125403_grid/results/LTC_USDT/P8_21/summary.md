# EMA Hourly Continuation — LTC/USDT P8_21

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.6300 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9841 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -3.2532 |
| sortino_ratio | -0.9921 |
| max_drawdown | 0.6850 |
| cagr | -0.3648 |
| net_avg_win | 52.8803 |
| net_avg_loss | -79.9203 |
| avg_hold_time_bars | 6.1804 |
| exposure | 0.1261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
