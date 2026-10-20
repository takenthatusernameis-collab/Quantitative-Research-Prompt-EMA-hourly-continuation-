# EMA Hourly Continuation — MLK/USDT P26_34

**Symbol:** MLK/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1328 |
| net_profit_factor | 0.1085 |
| net_win_rate | 0.1905 |
| gross_profit_factor | 0.4994 |
| gross_win_rate | 0.2244 |
| sharpe_ratio | -21.3493 |
| sortino_ratio | -11.8453 |
| max_drawdown | 1.0000 |
| cagr | -0.9984 |
| net_avg_win | 4.8113 |
| net_avg_loss | -10.4347 |
| avg_hold_time_bars | 2.2681 |
| exposure | 0.1363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
