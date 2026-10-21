# EMA Hourly Continuation — BNB/USDT P26_200

**Symbol:** BNB/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.7303 |
| net_win_rate | 0.5312 |
| gross_profit_factor | 1.1136 |
| gross_win_rate | 0.5312 |
| sharpe_ratio | -1.5879 |
| sortino_ratio | -0.4100 |
| max_drawdown | 0.4120 |
| cagr | -0.1689 |
| net_avg_win | 59.1673 |
| net_avg_loss | -91.8261 |
| avg_hold_time_bars | 39.0094 |
| exposure | 0.5674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
