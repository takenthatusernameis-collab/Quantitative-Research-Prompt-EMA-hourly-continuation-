# EMA Hourly Continuation — ARKM/USDT P21_200

**Symbol:** ARKM/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.8248 |
| net_win_rate | 0.4912 |
| gross_profit_factor | 0.9530 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -1.0831 |
| sortino_ratio | -0.2856 |
| max_drawdown | 0.3274 |
| cagr | -0.1249 |
| net_avg_win | 79.7877 |
| net_avg_loss | -93.4036 |
| avg_hold_time_bars | 38.1637 |
| exposure | 0.5933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
