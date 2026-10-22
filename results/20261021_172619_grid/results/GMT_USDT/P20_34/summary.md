# EMA Hourly Continuation — GMT/USDT P20_34

**Symbol:** GMT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.5996 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.8457 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -2.7782 |
| sortino_ratio | -0.7205 |
| max_drawdown | 0.5709 |
| cagr | -0.2807 |
| net_avg_win | 55.4476 |
| net_avg_loss | -79.4150 |
| avg_hold_time_bars | 5.1581 |
| exposure | 0.0771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
