# EMA Hourly Continuation — QI/USDT P21_144

**Symbol:** QI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.5754 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.8619 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -4.0023 |
| sortino_ratio | -1.2390 |
| max_drawdown | 0.7889 |
| cagr | -0.4503 |
| net_avg_win | 48.2083 |
| net_avg_loss | -67.4525 |
| avg_hold_time_bars | 23.2098 |
| exposure | 0.5157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
