# EMA Hourly Continuation — AERO/USDT P34_200

**Symbol:** AERO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.6823 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.9252 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -2.3429 |
| sortino_ratio | -0.6189 |
| max_drawdown | 0.5360 |
| cagr | -0.2526 |
| net_avg_win | 67.9332 |
| net_avg_loss | -88.7377 |
| avg_hold_time_bars | 31.7615 |
| exposure | 0.5024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
