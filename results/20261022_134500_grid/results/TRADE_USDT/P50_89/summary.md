# EMA Hourly Continuation — TRADE/USDT P50_89

**Symbol:** TRADE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.4450 |
| net_win_rate | 0.3963 |
| gross_profit_factor | 0.7267 |
| gross_win_rate | 0.4019 |
| sharpe_ratio | -6.4196 |
| sortino_ratio | -2.0887 |
| max_drawdown | 0.9317 |
| cagr | -0.6499 |
| net_avg_win | 35.1032 |
| net_avg_loss | -51.7803 |
| avg_hold_time_bars | 5.8486 |
| exposure | 0.1422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
