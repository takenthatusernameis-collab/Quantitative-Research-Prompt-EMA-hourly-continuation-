# EMA Hourly Continuation — BAND/USDT P12_200

**Symbol:** BAND/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.8919 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0793 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -0.6448 |
| sortino_ratio | -0.1663 |
| max_drawdown | 0.3463 |
| cagr | -0.0765 |
| net_avg_win | 88.7498 |
| net_avg_loss | -108.4991 |
| avg_hold_time_bars | 49.8025 |
| exposure | 0.7302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
