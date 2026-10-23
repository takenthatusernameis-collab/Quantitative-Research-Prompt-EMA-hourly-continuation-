# EMA Hourly Continuation — FLOW/USDT P12_34

**Symbol:** FLOW/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1286 |
| net_profit_factor | 0.4532 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.9035 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -9.2950 |
| sortino_ratio | -4.7213 |
| max_drawdown | 0.9971 |
| cagr | -0.8998 |
| net_avg_win | 14.8045 |
| net_avg_loss | -25.0411 |
| avg_hold_time_bars | 4.5054 |
| exposure | 0.2634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
