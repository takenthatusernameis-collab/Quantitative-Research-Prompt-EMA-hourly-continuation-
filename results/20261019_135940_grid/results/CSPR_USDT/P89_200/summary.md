# EMA Hourly Continuation — CSPR/USDT P89_200

**Symbol:** CSPR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.5562 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.8433 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -4.5062 |
| sortino_ratio | -1.4925 |
| max_drawdown | 0.8401 |
| cagr | -0.5110 |
| net_avg_win | 42.6619 |
| net_avg_loss | -61.2158 |
| avg_hold_time_bars | 8.9257 |
| exposure | 0.2240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
