# EMA Hourly Continuation — TNSR/USDT P8_12

**Symbol:** TNSR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1760 |
| net_profit_factor | 0.3971 |
| net_win_rate | 0.3858 |
| gross_profit_factor | 0.8901 |
| gross_win_rate | 0.4250 |
| sharpe_ratio | -15.0980 |
| sortino_ratio | -9.0107 |
| max_drawdown | 1.0000 |
| cagr | -0.9903 |
| net_avg_win | 9.6995 |
| net_avg_loss | -15.3431 |
| avg_hold_time_bars | 2.0136 |
| exposure | 0.1604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
