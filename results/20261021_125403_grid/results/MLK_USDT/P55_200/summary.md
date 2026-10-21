# EMA Hourly Continuation — MLK/USDT P55_200

**Symbol:** MLK/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.4774 |
| net_win_rate | 0.3671 |
| gross_profit_factor | 0.6226 |
| gross_win_rate | 0.3671 |
| sharpe_ratio | -4.3987 |
| sortino_ratio | -1.0991 |
| max_drawdown | 0.7295 |
| cagr | -0.4027 |
| net_avg_win | 57.2758 |
| net_avg_loss | -69.5918 |
| avg_hold_time_bars | 23.0696 |
| exposure | 0.3299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
