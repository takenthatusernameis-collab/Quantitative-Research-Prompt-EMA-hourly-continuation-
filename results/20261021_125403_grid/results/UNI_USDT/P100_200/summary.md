# EMA Hourly Continuation — UNI/USDT P100_200

**Symbol:** UNI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.9594 |
| net_win_rate | 0.5462 |
| gross_profit_factor | 1.1987 |
| gross_win_rate | 0.5462 |
| sharpe_ratio | -0.1460 |
| sortino_ratio | -0.0341 |
| max_drawdown | 0.1557 |
| cagr | -0.0198 |
| net_avg_win | 81.4604 |
| net_avg_loss | -102.1798 |
| avg_hold_time_bars | 11.5885 |
| exposure | 0.1370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
