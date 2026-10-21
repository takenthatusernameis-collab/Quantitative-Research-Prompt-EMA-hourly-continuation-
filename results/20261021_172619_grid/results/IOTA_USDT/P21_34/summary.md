# EMA Hourly Continuation — IOTA/USDT P21_34

**Symbol:** IOTA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.5711 |
| net_win_rate | 0.4601 |
| gross_profit_factor | 0.8262 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -2.9755 |
| sortino_ratio | -0.7686 |
| max_drawdown | 0.5987 |
| cagr | -0.2964 |
| net_avg_win | 52.0451 |
| net_avg_loss | -77.6733 |
| avg_hold_time_bars | 5.0613 |
| exposure | 0.0750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
