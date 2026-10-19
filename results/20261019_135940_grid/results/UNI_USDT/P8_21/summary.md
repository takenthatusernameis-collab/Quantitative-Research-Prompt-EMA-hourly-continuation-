# EMA Hourly Continuation — UNI/USDT P8_21

**Symbol:** UNI/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1684 |
| net_profit_factor | 0.4164 |
| net_win_rate | 0.4216 |
| gross_profit_factor | 0.8954 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -12.1737 |
| sortino_ratio | -7.0602 |
| max_drawdown | 0.9999 |
| cagr | -0.9712 |
| net_avg_win | 10.0466 |
| net_avg_loss | -17.5890 |
| avg_hold_time_bars | 2.7298 |
| exposure | 0.2090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
