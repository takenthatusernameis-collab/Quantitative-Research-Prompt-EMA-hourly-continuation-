# EMA Hourly Continuation — IOTA/USDT P20_55

**Symbol:** IOTA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.7241 |
| net_win_rate | 0.4861 |
| gross_profit_factor | 0.9711 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -2.5709 |
| sortino_ratio | -0.8559 |
| max_drawdown | 0.6495 |
| cagr | -0.3237 |
| net_avg_win | 62.4156 |
| net_avg_loss | -81.5491 |
| avg_hold_time_bars | 8.4455 |
| exposure | 0.2077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
