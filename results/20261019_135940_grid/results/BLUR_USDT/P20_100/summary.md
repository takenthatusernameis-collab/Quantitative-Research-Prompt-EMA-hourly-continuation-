# EMA Hourly Continuation — BLUR/USDT P20_100

**Symbol:** BLUR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 624 |
| net_profit_factor | 0.6651 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 1.0146 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -3.7560 |
| sortino_ratio | -1.3182 |
| max_drawdown | 0.8215 |
| cagr | -0.4701 |
| net_avg_win | 53.0300 |
| net_avg_loss | -73.3577 |
| avg_hold_time_bars | 16.5769 |
| exposure | 0.4681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
