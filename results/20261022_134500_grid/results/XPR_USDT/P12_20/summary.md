# EMA Hourly Continuation — XPR/USDT P12_20

**Symbol:** XPR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1355 |
| net_profit_factor | 0.2179 |
| net_win_rate | 0.3070 |
| gross_profit_factor | 0.6147 |
| gross_win_rate | 0.3439 |
| sharpe_ratio | -17.8242 |
| sortino_ratio | -9.7298 |
| max_drawdown | 1.0000 |
| cagr | -0.9953 |
| net_avg_win | 6.6980 |
| net_avg_loss | -13.6170 |
| avg_hold_time_bars | 2.1299 |
| exposure | 0.1312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
