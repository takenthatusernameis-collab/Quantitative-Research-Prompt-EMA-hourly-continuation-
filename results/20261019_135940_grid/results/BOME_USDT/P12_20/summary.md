# EMA Hourly Continuation — BOME/USDT P12_20

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1469 |
| net_profit_factor | 0.3882 |
| net_win_rate | 0.4139 |
| gross_profit_factor | 0.8374 |
| gross_win_rate | 0.4384 |
| sharpe_ratio | -11.8702 |
| sortino_ratio | -6.4077 |
| max_drawdown | 0.9997 |
| cagr | -0.9629 |
| net_avg_win | 10.4319 |
| net_avg_loss | -18.9779 |
| avg_hold_time_bars | 2.0327 |
| exposure | 0.1357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
