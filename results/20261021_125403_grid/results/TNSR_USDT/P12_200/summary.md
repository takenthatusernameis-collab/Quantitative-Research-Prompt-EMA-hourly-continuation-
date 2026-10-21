# EMA Hourly Continuation — TNSR/USDT P12_200

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.7448 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.8764 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -1.7570 |
| sortino_ratio | -0.4322 |
| max_drawdown | 0.4300 |
| cagr | -0.1812 |
| net_avg_win | 82.5792 |
| net_avg_loss | -95.2289 |
| avg_hold_time_bars | 52.8416 |
| exposure | 0.7246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
