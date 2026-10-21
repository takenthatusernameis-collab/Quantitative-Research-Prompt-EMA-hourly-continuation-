# EMA Hourly Continuation — BLUR/USDT P21_50

**Symbol:** BLUR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.7319 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9866 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.2110 |
| sortino_ratio | -0.7433 |
| max_drawdown | 0.6289 |
| cagr | -0.2881 |
| net_avg_win | 56.9565 |
| net_avg_loss | -77.8155 |
| avg_hold_time_bars | 7.1105 |
| exposure | 0.1776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
