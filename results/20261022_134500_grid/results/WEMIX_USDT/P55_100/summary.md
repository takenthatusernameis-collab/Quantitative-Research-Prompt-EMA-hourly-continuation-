# EMA Hourly Continuation — WEMIX/USDT P55_100

**Symbol:** WEMIX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1022 |
| net_profit_factor | 0.2334 |
| net_win_rate | 0.2847 |
| gross_profit_factor | 0.4410 |
| gross_win_rate | 0.3072 |
| sharpe_ratio | -14.4832 |
| sortino_ratio | -6.7516 |
| max_drawdown | 0.9998 |
| cagr | -0.9687 |
| net_avg_win | 10.4623 |
| net_avg_loss | -17.8425 |
| avg_hold_time_bars | 4.2055 |
| exposure | 0.1954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
