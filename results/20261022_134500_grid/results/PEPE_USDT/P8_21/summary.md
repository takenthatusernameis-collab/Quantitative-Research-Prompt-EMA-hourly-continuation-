# EMA Hourly Continuation — PEPE/USDT P8_21

**Symbol:** PEPE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1709 |
| net_profit_factor | 0.4791 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.8426 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -11.3602 |
| sortino_ratio | -6.6006 |
| max_drawdown | 0.9998 |
| cagr | -0.9646 |
| net_avg_win | 12.3264 |
| net_avg_loss | -19.9306 |
| avg_hold_time_bars | 2.5793 |
| exposure | 0.2004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
