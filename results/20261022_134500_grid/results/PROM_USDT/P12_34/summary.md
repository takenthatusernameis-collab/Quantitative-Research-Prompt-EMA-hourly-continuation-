# EMA Hourly Continuation — PROM/USDT P12_34

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1228 |
| net_profit_factor | 0.4835 |
| net_win_rate | 0.4145 |
| gross_profit_factor | 0.9385 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -9.9174 |
| sortino_ratio | -4.8851 |
| max_drawdown | 0.9979 |
| cagr | -0.9138 |
| net_avg_win | 18.3538 |
| net_avg_loss | -26.8719 |
| avg_hold_time_bars | 5.4039 |
| exposure | 0.3016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
