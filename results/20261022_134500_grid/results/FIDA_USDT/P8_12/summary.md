# EMA Hourly Continuation — FIDA/USDT P8_12

**Symbol:** FIDA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1653 |
| net_profit_factor | 0.2620 |
| net_win_rate | 0.3975 |
| gross_profit_factor | 0.7433 |
| gross_win_rate | 0.4404 |
| sharpe_ratio | -14.1078 |
| sortino_ratio | -8.2001 |
| max_drawdown | 1.0000 |
| cagr | -0.9844 |
| net_avg_win | 5.4034 |
| net_avg_loss | -13.6041 |
| avg_hold_time_bars | 2.5469 |
| exposure | 0.1905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
