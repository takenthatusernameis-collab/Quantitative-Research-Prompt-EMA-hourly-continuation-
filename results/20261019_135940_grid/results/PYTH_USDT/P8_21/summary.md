# EMA Hourly Continuation — PYTH/USDT P8_21

**Symbol:** PYTH/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1612 |
| net_profit_factor | 0.4705 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.9491 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -9.6600 |
| sortino_ratio | -5.4191 |
| max_drawdown | 0.9990 |
| cagr | -0.9351 |
| net_avg_win | 11.9143 |
| net_avg_loss | -21.7598 |
| avg_hold_time_bars | 2.9932 |
| exposure | 0.2193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
