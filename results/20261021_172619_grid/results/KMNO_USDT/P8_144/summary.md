# EMA Hourly Continuation — KMNO/USDT P8_144

**Symbol:** KMNO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.8285 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 0.9770 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -1.1406 |
| sortino_ratio | -0.3055 |
| max_drawdown | 0.3081 |
| cagr | -0.1332 |
| net_avg_win | 84.0798 |
| net_avg_loss | -98.6044 |
| avg_hold_time_bars | 46.2594 |
| exposure | 0.7411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
