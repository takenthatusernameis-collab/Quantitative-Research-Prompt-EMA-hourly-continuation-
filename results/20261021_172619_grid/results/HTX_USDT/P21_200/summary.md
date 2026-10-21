# EMA Hourly Continuation — HTX/USDT P21_200

**Symbol:** HTX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.6409 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9578 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -2.6722 |
| sortino_ratio | -0.6449 |
| max_drawdown | 0.5700 |
| cagr | -0.2628 |
| net_avg_win | 69.4024 |
| net_avg_loss | -99.6241 |
| avg_hold_time_bars | 49.2535 |
| exposure | 0.6419 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
