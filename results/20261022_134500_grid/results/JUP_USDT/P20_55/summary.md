# EMA Hourly Continuation — JUP/USDT P20_55

**Symbol:** JUP/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 919 |
| net_profit_factor | 0.5720 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9356 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -5.2084 |
| sortino_ratio | -2.2284 |
| max_drawdown | 0.9338 |
| cagr | -0.6561 |
| net_avg_win | 28.4242 |
| net_avg_loss | -45.2485 |
| avg_hold_time_bars | 5.5267 |
| exposure | 0.2309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
