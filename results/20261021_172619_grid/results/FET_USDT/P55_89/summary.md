# EMA Hourly Continuation — FET/USDT P55_89

**Symbol:** FET/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.7907 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0023 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -1.1276 |
| sortino_ratio | -0.2620 |
| max_drawdown | 0.2982 |
| cagr | -0.1136 |
| net_avg_win | 74.7851 |
| net_avg_loss | -96.0319 |
| avg_hold_time_bars | 8.2443 |
| exposure | 0.0982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
