# EMA Hourly Continuation — ZBCN/USDT P12_50

**Symbol:** ZBCN/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1219 |
| net_profit_factor | 0.5972 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9279 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -5.3375 |
| sortino_ratio | -2.6280 |
| max_drawdown | 0.9582 |
| cagr | -0.7232 |
| net_avg_win | 24.1524 |
| net_avg_loss | -37.6881 |
| avg_hold_time_bars | 5.6957 |
| exposure | 0.3212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
