# EMA Hourly Continuation — NOT/USDT P12_21

**Symbol:** NOT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1480 |
| net_profit_factor | 0.4056 |
| net_win_rate | 0.4088 |
| gross_profit_factor | 0.8076 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -12.9321 |
| sortino_ratio | -7.1480 |
| max_drawdown | 0.9999 |
| cagr | -0.9759 |
| net_avg_win | 11.2770 |
| net_avg_loss | -19.2245 |
| avg_hold_time_bars | 2.1554 |
| exposure | 0.1498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
