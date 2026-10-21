# EMA Hourly Continuation — DODO/USDT P89_200

**Symbol:** DODO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.6013 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.7584 |
| gross_win_rate | 0.4357 |
| sharpe_ratio | -2.8409 |
| sortino_ratio | -0.7426 |
| max_drawdown | 0.5938 |
| cagr | -0.2895 |
| net_avg_win | 58.4843 |
| net_avg_loss | -75.0859 |
| avg_hold_time_bars | 12.2865 |
| exposure | 0.1901 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
