# EMA Hourly Continuation — STRAX/USDT P8_26

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1420 |
| net_profit_factor | 0.4447 |
| net_win_rate | 0.4035 |
| gross_profit_factor | 0.7942 |
| gross_win_rate | 0.4289 |
| sharpe_ratio | -11.3706 |
| sortino_ratio | -6.0407 |
| max_drawdown | 0.9995 |
| cagr | -0.9527 |
| net_avg_win | 13.9704 |
| net_avg_loss | -21.2516 |
| avg_hold_time_bars | 4.8958 |
| exposure | 0.3178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
