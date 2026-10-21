# EMA Hourly Continuation — ATOM/USDT P20_100

**Symbol:** ATOM/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.7668 |
| net_win_rate | 0.5023 |
| gross_profit_factor | 0.9810 |
| gross_win_rate | 0.5023 |
| sharpe_ratio | -1.5549 |
| sortino_ratio | -0.4676 |
| max_drawdown | 0.4586 |
| cagr | -0.1943 |
| net_avg_win | 62.3020 |
| net_avg_loss | -81.9948 |
| avg_hold_time_bars | 20.2295 |
| exposure | 0.4046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
