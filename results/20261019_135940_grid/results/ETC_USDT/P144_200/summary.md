# EMA Hourly Continuation — ETC/USDT P144_200

**Symbol:** ETC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.4051 |
| net_win_rate | 0.4317 |
| gross_profit_factor | 0.9059 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -6.1964 |
| sortino_ratio | -1.8112 |
| max_drawdown | 0.8978 |
| cagr | -0.5957 |
| net_avg_win | 33.9454 |
| net_avg_loss | -63.6353 |
| avg_hold_time_bars | 4.4844 |
| exposure | 0.0850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
