# EMA Hourly Continuation — FLOW/USDT P8_20

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1785 |
| net_profit_factor | 0.2585 |
| net_win_rate | 0.4028 |
| gross_profit_factor | 0.6729 |
| gross_win_rate | 0.4336 |
| sharpe_ratio | -14.1375 |
| sortino_ratio | -8.5016 |
| max_drawdown | 1.0000 |
| cagr | -0.9863 |
| net_avg_win | 4.8491 |
| net_avg_loss | -12.6513 |
| avg_hold_time_bars | 2.7361 |
| exposure | 0.2220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
