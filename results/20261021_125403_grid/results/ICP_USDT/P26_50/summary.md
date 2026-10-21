# EMA Hourly Continuation — ICP/USDT P26_50

**Symbol:** ICP/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.6860 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9225 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -2.2335 |
| sortino_ratio | -0.6064 |
| max_drawdown | 0.5136 |
| cagr | -0.2429 |
| net_avg_win | 63.5091 |
| net_avg_loss | -85.6456 |
| avg_hold_time_bars | 6.5778 |
| exposure | 0.1076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
