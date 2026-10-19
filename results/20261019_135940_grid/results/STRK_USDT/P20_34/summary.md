# EMA Hourly Continuation — STRK/USDT P20_34

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1123 |
| net_profit_factor | 0.3764 |
| net_win_rate | 0.4248 |
| gross_profit_factor | 0.7689 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -9.2946 |
| sortino_ratio | -4.4246 |
| max_drawdown | 0.9959 |
| cagr | -0.8863 |
| net_avg_win | 12.5986 |
| net_avg_loss | -24.7167 |
| avg_hold_time_bars | 2.7035 |
| exposure | 0.1380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
