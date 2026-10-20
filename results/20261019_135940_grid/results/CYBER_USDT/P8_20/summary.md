# EMA Hourly Continuation — CYBER/USDT P8_20

**Symbol:** CYBER/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1622 |
| net_profit_factor | 0.4208 |
| net_win_rate | 0.4353 |
| gross_profit_factor | 0.8599 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -11.3597 |
| sortino_ratio | -6.4589 |
| max_drawdown | 0.9997 |
| cagr | -0.9612 |
| net_avg_win | 10.2886 |
| net_avg_loss | -18.8438 |
| avg_hold_time_bars | 3.3101 |
| exposure | 0.2440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
