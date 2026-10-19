# EMA Hourly Continuation — PEPE/USDT P26_89

**Symbol:** PEPE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.5542 |
| net_win_rate | 0.4435 |
| gross_profit_factor | 0.8670 |
| gross_win_rate | 0.4435 |
| sharpe_ratio | -5.6960 |
| sortino_ratio | -2.0519 |
| max_drawdown | 0.9273 |
| cagr | -0.6432 |
| net_avg_win | 38.5812 |
| net_avg_loss | -55.4695 |
| avg_hold_time_bars | 9.9449 |
| exposure | 0.3038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
