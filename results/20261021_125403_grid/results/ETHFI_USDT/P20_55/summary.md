# EMA Hourly Continuation — ETHFI/USDT P20_55

**Symbol:** ETHFI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.7364 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.9096 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -2.4428 |
| sortino_ratio | -0.7843 |
| max_drawdown | 0.6246 |
| cagr | -0.3029 |
| net_avg_win | 69.9427 |
| net_avg_loss | -83.4137 |
| avg_hold_time_bars | 8.9037 |
| exposure | 0.2060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
