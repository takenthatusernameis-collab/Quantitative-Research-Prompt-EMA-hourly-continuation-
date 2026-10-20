# EMA Hourly Continuation — EWT/USDT P20_26

**Symbol:** EWT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1056 |
| net_profit_factor | 0.2443 |
| net_win_rate | 0.3106 |
| gross_profit_factor | 0.6139 |
| gross_win_rate | 0.3504 |
| sharpe_ratio | -15.2282 |
| sortino_ratio | -7.2854 |
| max_drawdown | 1.0000 |
| cagr | -0.9821 |
| net_avg_win | 9.8568 |
| net_avg_loss | -18.1767 |
| avg_hold_time_bars | 2.6544 |
| exposure | 0.1274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
