# EMA Hourly Continuation — DOGS/USDT P21_100

**Symbol:** DOGS/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.8616 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0419 |
| gross_win_rate | 0.5139 |
| sharpe_ratio | -0.9196 |
| sortino_ratio | -0.2843 |
| max_drawdown | 0.2580 |
| cagr | -0.1256 |
| net_avg_win | 76.5227 |
| net_avg_loss | -93.8784 |
| avg_hold_time_bars | 18.1662 |
| exposure | 0.3826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
