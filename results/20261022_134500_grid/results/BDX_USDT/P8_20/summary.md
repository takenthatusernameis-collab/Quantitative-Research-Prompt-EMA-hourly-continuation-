# EMA Hourly Continuation — BDX/USDT P8_20

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1935 |
| net_profit_factor | 0.1776 |
| net_win_rate | 0.1922 |
| gross_profit_factor | 0.5215 |
| gross_win_rate | 0.2718 |
| sharpe_ratio | -27.7994 |
| sortino_ratio | -19.4536 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 5.8058 |
| net_avg_loss | -7.7798 |
| avg_hold_time_bars | 2.1390 |
| exposure | 0.1881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
