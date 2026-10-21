# EMA Hourly Continuation — FIL/USDT P89_200

**Symbol:** FIL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.8184 |
| net_win_rate | 0.5146 |
| gross_profit_factor | 1.0465 |
| gross_win_rate | 0.5146 |
| sharpe_ratio | -0.9073 |
| sortino_ratio | -0.2017 |
| max_drawdown | 0.3160 |
| cagr | -0.0893 |
| net_avg_win | 76.7476 |
| net_avg_loss | -99.4315 |
| avg_hold_time_bars | 15.9079 |
| exposure | 0.1728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
