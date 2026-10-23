# EMA Hourly Continuation — UQC/USDT P21_200

**Symbol:** UQC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 183 |
| net_profit_factor | 0.3971 |
| net_win_rate | 0.3224 |
| gross_profit_factor | 0.5093 |
| gross_win_rate | 0.3279 |
| sharpe_ratio | -3.9864 |
| sortino_ratio | -0.7485 |
| max_drawdown | 0.5976 |
| cagr | -0.3006 |
| net_avg_win | 66.3132 |
| net_avg_loss | -79.4655 |
| avg_hold_time_bars | 89.0273 |
| exposure | 0.7374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
