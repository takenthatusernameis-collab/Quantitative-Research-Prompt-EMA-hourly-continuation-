# EMA Hourly Continuation — AURORA/USDT P89_100

**Symbol:** AURORA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 107 |
| net_profit_factor | 0.4887 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.7916 |
| gross_win_rate | 0.4393 |
| sharpe_ratio | -2.2950 |
| sortino_ratio | -0.3413 |
| max_drawdown | 0.3428 |
| cagr | -0.1457 |
| net_avg_win | 66.4377 |
| net_avg_loss | -106.4919 |
| avg_hold_time_bars | 4.7196 |
| exposure | 0.0230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
