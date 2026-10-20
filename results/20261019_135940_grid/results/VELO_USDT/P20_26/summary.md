# EMA Hourly Continuation — VELO/USDT P20_26

**Symbol:** VELO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1284 |
| net_profit_factor | 0.4098 |
| net_win_rate | 0.3840 |
| gross_profit_factor | 0.7881 |
| gross_win_rate | 0.4151 |
| sharpe_ratio | -12.6686 |
| sortino_ratio | -6.4746 |
| max_drawdown | 0.9998 |
| cagr | -0.9650 |
| net_avg_win | 14.0790 |
| net_avg_loss | -21.4143 |
| avg_hold_time_bars | 1.9058 |
| exposure | 0.1112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
