# EMA Hourly Continuation — MOCA/USDT P8_34

**Symbol:** MOCA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.7187 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9412 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -2.8092 |
| sortino_ratio | -1.0965 |
| max_drawdown | 0.7030 |
| cagr | -0.3947 |
| net_avg_win | 52.5702 |
| net_avg_loss | -70.1826 |
| avg_hold_time_bars | 8.3047 |
| exposure | 0.2814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
