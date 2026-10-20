# EMA Hourly Continuation — GALA/USDT P8_50

**Symbol:** GALA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1105 |
| net_profit_factor | 0.4992 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.7968 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -6.7934 |
| sortino_ratio | -3.1706 |
| max_drawdown | 0.9802 |
| cagr | -0.7862 |
| net_avg_win | 19.7994 |
| net_avg_loss | -31.9500 |
| avg_hold_time_bars | 9.1140 |
| exposure | 0.4578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
