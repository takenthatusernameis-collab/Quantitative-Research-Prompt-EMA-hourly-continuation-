# EMA Hourly Continuation — HBAR/USDT P20_200

**Symbol:** HBAR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6989 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0341 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -2.1409 |
| sortino_ratio | -0.5888 |
| max_drawdown | 0.5298 |
| cagr | -0.2472 |
| net_avg_win | 60.3904 |
| net_avg_loss | -89.6083 |
| avg_hold_time_bars | 36.8519 |
| exposure | 0.6449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
