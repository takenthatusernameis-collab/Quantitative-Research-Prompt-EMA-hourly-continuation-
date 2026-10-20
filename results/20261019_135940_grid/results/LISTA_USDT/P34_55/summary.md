# EMA Hourly Continuation — LISTA/USDT P34_55

**Symbol:** LISTA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 775 |
| net_profit_factor | 0.4516 |
| net_win_rate | 0.4503 |
| gross_profit_factor | 0.7960 |
| gross_win_rate | 0.4594 |
| sharpe_ratio | -6.5210 |
| sortino_ratio | -2.6568 |
| max_drawdown | 0.9507 |
| cagr | -0.7226 |
| net_avg_win | 22.4130 |
| net_avg_loss | -40.6594 |
| avg_hold_time_bars | 4.3368 |
| exposure | 0.1643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
