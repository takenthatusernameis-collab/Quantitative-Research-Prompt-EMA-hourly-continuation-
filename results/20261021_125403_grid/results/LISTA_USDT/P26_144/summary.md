# EMA Hourly Continuation — LISTA/USDT P26_144

**Symbol:** LISTA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7525 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.8997 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -1.7727 |
| sortino_ratio | -0.5055 |
| max_drawdown | 0.4267 |
| cagr | -0.2088 |
| net_avg_win | 71.9244 |
| net_avg_loss | -86.8051 |
| avg_hold_time_bars | 24.5107 |
| exposure | 0.4482 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
