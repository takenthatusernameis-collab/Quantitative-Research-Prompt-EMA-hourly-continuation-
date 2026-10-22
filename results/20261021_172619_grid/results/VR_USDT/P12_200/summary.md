# EMA Hourly Continuation — VR/USDT P12_200

**Symbol:** VR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.7329 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.8733 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -1.8515 |
| sortino_ratio | -0.4578 |
| max_drawdown | 0.4356 |
| cagr | -0.1926 |
| net_avg_win | 80.8864 |
| net_avg_loss | -94.8843 |
| avg_hold_time_bars | 48.8197 |
| exposure | 0.6768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
