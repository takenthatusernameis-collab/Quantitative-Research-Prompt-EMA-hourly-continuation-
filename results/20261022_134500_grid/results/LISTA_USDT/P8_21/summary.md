# EMA Hourly Continuation — LISTA/USDT P8_21

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1324 |
| net_profit_factor | 0.6026 |
| net_win_rate | 0.4388 |
| gross_profit_factor | 1.0306 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -8.7884 |
| sortino_ratio | -4.6525 |
| max_drawdown | 0.9954 |
| cagr | -0.8982 |
| net_avg_win | 25.9703 |
| net_avg_loss | -33.7019 |
| avg_hold_time_bars | 4.0166 |
| exposure | 0.2600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
