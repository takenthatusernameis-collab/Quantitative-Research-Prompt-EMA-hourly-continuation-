# EMA Hourly Continuation — LINK/USDT P89_100

**Symbol:** LINK/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 73 |
| net_profit_factor | 0.8188 |
| net_win_rate | 0.5479 |
| gross_profit_factor | 1.1929 |
| gross_win_rate | 0.5479 |
| sharpe_ratio | -0.4880 |
| sortino_ratio | -0.0605 |
| max_drawdown | 0.1091 |
| cagr | -0.0275 |
| net_avg_win | 76.4844 |
| net_avg_loss | -113.2254 |
| avg_hold_time_bars | 5.5479 |
| exposure | 0.0184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
