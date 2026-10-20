# EMA Hourly Continuation — LISTA/USDT P20_200

**Symbol:** LISTA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.6715 |
| net_win_rate | 0.4654 |
| gross_profit_factor | 0.9093 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -2.6679 |
| sortino_ratio | -0.8004 |
| max_drawdown | 0.6003 |
| cagr | -0.3117 |
| net_avg_win | 60.9960 |
| net_avg_loss | -79.0741 |
| avg_hold_time_bars | 27.5251 |
| exposure | 0.5639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
