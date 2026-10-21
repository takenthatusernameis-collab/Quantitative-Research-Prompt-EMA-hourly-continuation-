# EMA Hourly Continuation — ETHFI/USDT P26_55

**Symbol:** ETHFI/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.7517 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9427 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -2.0063 |
| sortino_ratio | -0.5904 |
| max_drawdown | 0.5287 |
| cagr | -0.2383 |
| net_avg_win | 73.4995 |
| net_avg_loss | -90.2541 |
| avg_hold_time_bars | 7.8071 |
| exposure | 0.1508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
