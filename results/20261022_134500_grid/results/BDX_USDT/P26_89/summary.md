# EMA Hourly Continuation — BDX/USDT P26_89

**Symbol:** BDX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1253 |
| net_profit_factor | 0.2924 |
| net_win_rate | 0.2977 |
| gross_profit_factor | 0.6881 |
| gross_win_rate | 0.3496 |
| sharpe_ratio | -17.6215 |
| sortino_ratio | -9.3106 |
| max_drawdown | 1.0000 |
| cagr | -0.9943 |
| net_avg_win | 11.0765 |
| net_avg_loss | -16.0585 |
| avg_hold_time_bars | 4.4038 |
| exposure | 0.2508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
