# EMA Hourly Continuation — PENDLE/USDT P26_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.7510 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.8713 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -1.4060 |
| sortino_ratio | -0.3202 |
| max_drawdown | 0.3768 |
| cagr | -0.1375 |
| net_avg_win | 78.0247 |
| net_avg_loss | -90.9973 |
| avg_hold_time_bars | 54.8911 |
| exposure | 0.6412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
