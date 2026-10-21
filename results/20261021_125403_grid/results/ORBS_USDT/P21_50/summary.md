# EMA Hourly Continuation — ORBS/USDT P21_50

**Symbol:** ORBS/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.5500 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.8215 |
| gross_win_rate | 0.4304 |
| sharpe_ratio | -4.9774 |
| sortino_ratio | -1.6588 |
| max_drawdown | 0.8570 |
| cagr | -0.5341 |
| net_avg_win | 44.5547 |
| net_avg_loss | -60.7600 |
| avg_hold_time_bars | 8.9084 |
| exposure | 0.2211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
