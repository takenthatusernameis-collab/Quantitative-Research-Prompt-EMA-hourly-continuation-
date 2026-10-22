# EMA Hourly Continuation — PYTH/USDT P20_50

**Symbol:** PYTH/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 987 |
| net_profit_factor | 0.5619 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.9397 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -5.3483 |
| sortino_ratio | -2.3711 |
| max_drawdown | 0.9428 |
| cagr | -0.6786 |
| net_avg_win | 25.3916 |
| net_avg_loss | -42.0908 |
| avg_hold_time_bars | 4.7133 |
| exposure | 0.2115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
