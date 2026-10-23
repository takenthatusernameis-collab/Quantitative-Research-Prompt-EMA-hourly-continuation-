# EMA Hourly Continuation — KSM/USDT P20_100

**Symbol:** KSM/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.5458 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.8671 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -4.4321 |
| sortino_ratio | -1.5220 |
| max_drawdown | 0.8525 |
| cagr | -0.5238 |
| net_avg_win | 36.6477 |
| net_avg_loss | -57.4050 |
| avg_hold_time_bars | 16.7704 |
| exposure | 0.4581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
