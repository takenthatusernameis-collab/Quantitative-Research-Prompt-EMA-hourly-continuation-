# EMA Hourly Continuation — GRAM/USDT P100_200

**Symbol:** GRAM/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.7054 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9818 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -1.7323 |
| sortino_ratio | -0.4108 |
| max_drawdown | 0.3976 |
| cagr | -0.1715 |
| net_avg_win | 66.3042 |
| net_avg_loss | -93.3102 |
| avg_hold_time_bars | 12.2125 |
| exposure | 0.1515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
