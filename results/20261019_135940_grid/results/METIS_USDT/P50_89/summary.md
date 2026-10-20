# EMA Hourly Continuation — METIS/USDT P50_89

**Symbol:** METIS/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.4261 |
| net_win_rate | 0.4131 |
| gross_profit_factor | 0.7908 |
| gross_win_rate | 0.4365 |
| sharpe_ratio | -7.0915 |
| sortino_ratio | -2.6312 |
| max_drawdown | 0.9613 |
| cagr | -0.7244 |
| net_avg_win | 25.2023 |
| net_avg_loss | -41.6399 |
| avg_hold_time_bars | 4.6949 |
| exposure | 0.1462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
