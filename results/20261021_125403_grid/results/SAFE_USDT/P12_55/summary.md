# EMA Hourly Continuation — SAFE/USDT P12_55

**Symbol:** SAFE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.7586 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9567 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -2.0374 |
| sortino_ratio | -0.7214 |
| max_drawdown | 0.5728 |
| cagr | -0.2833 |
| net_avg_win | 58.8845 |
| net_avg_loss | -75.8625 |
| avg_hold_time_bars | 13.7652 |
| exposure | 0.3839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
