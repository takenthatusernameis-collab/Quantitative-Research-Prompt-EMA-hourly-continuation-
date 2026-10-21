# EMA Hourly Continuation — CSPR/USDT P21_34

**Symbol:** CSPR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.6748 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.9032 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -2.2034 |
| sortino_ratio | -0.5117 |
| max_drawdown | 0.4821 |
| cagr | -0.2091 |
| net_avg_win | 75.0970 |
| net_avg_loss | -96.3999 |
| avg_hold_time_bars | 6.4491 |
| exposure | 0.0777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
