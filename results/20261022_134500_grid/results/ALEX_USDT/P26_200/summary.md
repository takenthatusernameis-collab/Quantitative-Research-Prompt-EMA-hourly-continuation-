# EMA Hourly Continuation — ALEX/USDT P26_200

**Symbol:** ALEX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.6160 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.8163 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -2.8674 |
| sortino_ratio | -0.7201 |
| max_drawdown | 0.6105 |
| cagr | -0.2908 |
| net_avg_win | 65.7622 |
| net_avg_loss | -82.7062 |
| avg_hold_time_bars | 41.9752 |
| exposure | 0.6163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
