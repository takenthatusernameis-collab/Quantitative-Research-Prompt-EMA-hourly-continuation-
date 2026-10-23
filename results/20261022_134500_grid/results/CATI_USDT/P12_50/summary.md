# EMA Hourly Continuation — CATI/USDT P12_50

**Symbol:** CATI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 923 |
| net_profit_factor | 0.4893 |
| net_win_rate | 0.4020 |
| gross_profit_factor | 0.7446 |
| gross_win_rate | 0.4171 |
| sharpe_ratio | -8.7306 |
| sortino_ratio | -4.1177 |
| max_drawdown | 0.9850 |
| cagr | -0.8634 |
| net_avg_win | 25.4183 |
| net_avg_loss | -34.9129 |
| avg_hold_time_bars | 7.4810 |
| exposure | 0.3785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
