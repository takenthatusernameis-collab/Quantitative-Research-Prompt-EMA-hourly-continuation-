# EMA Hourly Continuation — FIDA/USDT P26_55

**Symbol:** FIDA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 872 |
| net_profit_factor | 0.4573 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8890 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -6.7915 |
| sortino_ratio | -2.8219 |
| max_drawdown | 0.9698 |
| cagr | -0.7480 |
| net_avg_win | 21.1520 |
| net_avg_loss | -36.7402 |
| avg_hold_time_bars | 5.3819 |
| exposure | 0.2124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
