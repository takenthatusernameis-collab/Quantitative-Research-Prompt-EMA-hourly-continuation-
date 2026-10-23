# EMA Hourly Continuation — TFUEL/USDT P55_100

**Symbol:** TFUEL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.4219 |
| net_win_rate | 0.3871 |
| gross_profit_factor | 0.7832 |
| gross_win_rate | 0.4090 |
| sharpe_ratio | -8.5116 |
| sortino_ratio | -3.2488 |
| max_drawdown | 0.9837 |
| cagr | -0.8028 |
| net_avg_win | 25.3621 |
| net_avg_loss | -37.9711 |
| avg_hold_time_bars | 4.9398 |
| exposure | 0.1634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
