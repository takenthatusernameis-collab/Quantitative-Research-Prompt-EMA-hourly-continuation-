# EMA Hourly Continuation — SUSHI/USDT P8_144

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.5881 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.8627 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -3.7111 |
| sortino_ratio | -1.1926 |
| max_drawdown | 0.7798 |
| cagr | -0.4396 |
| net_avg_win | 45.1241 |
| net_avg_loss | -64.9639 |
| avg_hold_time_bars | 30.3528 |
| exposure | 0.7280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
