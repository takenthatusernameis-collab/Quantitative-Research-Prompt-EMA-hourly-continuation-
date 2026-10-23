# EMA Hourly Continuation — LISTA/USDT P55_89

**Symbol:** LISTA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 587 |
| net_profit_factor | 0.4547 |
| net_win_rate | 0.4276 |
| gross_profit_factor | 0.7570 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -5.8834 |
| sortino_ratio | -2.0815 |
| max_drawdown | 0.9089 |
| cagr | -0.6376 |
| net_avg_win | 30.1188 |
| net_avg_loss | -49.4775 |
| avg_hold_time_bars | 5.6848 |
| exposure | 0.1632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
