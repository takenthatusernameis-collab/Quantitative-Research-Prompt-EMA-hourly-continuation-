# EMA Hourly Continuation — ORBS/USDT P21_200

**Symbol:** ORBS/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6407 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.9320 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -3.4239 |
| sortino_ratio | -1.0091 |
| max_drawdown | 0.7060 |
| cagr | -0.3787 |
| net_avg_win | 63.1270 |
| net_avg_loss | -80.5366 |
| avg_hold_time_bars | 32.2580 |
| exposure | 0.6422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
