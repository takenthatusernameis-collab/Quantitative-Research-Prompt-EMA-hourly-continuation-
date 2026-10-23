# EMA Hourly Continuation — T/USDT P50_100

**Symbol:** T/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.4565 |
| net_win_rate | 0.4352 |
| gross_profit_factor | 0.8139 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -5.6153 |
| sortino_ratio | -1.8318 |
| max_drawdown | 0.8998 |
| cagr | -0.5943 |
| net_avg_win | 32.0670 |
| net_avg_loss | -54.1265 |
| avg_hold_time_bars | 8.6167 |
| exposure | 0.2106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
