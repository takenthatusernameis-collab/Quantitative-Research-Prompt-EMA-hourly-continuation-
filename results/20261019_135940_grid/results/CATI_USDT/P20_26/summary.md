# EMA Hourly Continuation — CATI/USDT P20_26

**Symbol:** CATI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1132 |
| net_profit_factor | 0.2784 |
| net_win_rate | 0.3348 |
| gross_profit_factor | 0.5971 |
| gross_win_rate | 0.3860 |
| sharpe_ratio | -16.0140 |
| sortino_ratio | -8.5882 |
| max_drawdown | 0.9999 |
| cagr | -0.9902 |
| net_avg_win | 10.1813 |
| net_avg_loss | -18.4038 |
| avg_hold_time_bars | 2.0159 |
| exposure | 0.1251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
