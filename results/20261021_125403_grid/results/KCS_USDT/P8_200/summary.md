# EMA Hourly Continuation — KCS/USDT P8_200

**Symbol:** KCS/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.5889 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.8575 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -2.6178 |
| sortino_ratio | -0.6278 |
| max_drawdown | 0.5406 |
| cagr | -0.2529 |
| net_avg_win | 55.9023 |
| net_avg_loss | -83.6174 |
| avg_hold_time_bars | 61.4366 |
| exposure | 0.7931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
