# EMA Hourly Continuation — AVAX/USDT P12_55

**Symbol:** AVAX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1019 |
| net_profit_factor | 0.5891 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.9795 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -7.1795 |
| sortino_ratio | -3.2228 |
| max_drawdown | 0.9815 |
| cagr | -0.7925 |
| net_avg_win | 30.9760 |
| net_avg_loss | -42.2484 |
| avg_hold_time_bars | 7.8086 |
| exposure | 0.3617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
