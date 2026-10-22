# EMA Hourly Continuation — POKT/USDT P8_26

**Symbol:** POKT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.6071 |
| net_win_rate | 0.4246 |
| gross_profit_factor | 0.8074 |
| gross_win_rate | 0.4246 |
| sharpe_ratio | -4.9630 |
| sortino_ratio | -1.8766 |
| max_drawdown | 0.8900 |
| cagr | -0.5809 |
| net_avg_win | 45.1622 |
| net_avg_loss | -54.8883 |
| avg_hold_time_bars | 6.2193 |
| exposure | 0.2015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
