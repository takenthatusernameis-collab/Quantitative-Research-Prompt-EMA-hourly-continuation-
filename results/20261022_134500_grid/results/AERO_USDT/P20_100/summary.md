# EMA Hourly Continuation — AERO/USDT P20_100

**Symbol:** AERO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.8182 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.1088 |
| gross_win_rate | 0.5235 |
| sharpe_ratio | -1.6485 |
| sortino_ratio | -0.5631 |
| max_drawdown | 0.5335 |
| cagr | -0.2335 |
| net_avg_win | 73.3113 |
| net_avg_loss | -97.0706 |
| avg_hold_time_bars | 15.7130 |
| exposure | 0.4107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
