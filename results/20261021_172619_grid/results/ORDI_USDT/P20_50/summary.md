# EMA Hourly Continuation — ORDI/USDT P20_50

**Symbol:** ORDI/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.7196 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.9225 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -2.6266 |
| sortino_ratio | -0.8356 |
| max_drawdown | 0.6345 |
| cagr | -0.3188 |
| net_avg_win | 67.8395 |
| net_avg_loss | -83.5631 |
| avg_hold_time_bars | 7.3795 |
| exposure | 0.1670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
