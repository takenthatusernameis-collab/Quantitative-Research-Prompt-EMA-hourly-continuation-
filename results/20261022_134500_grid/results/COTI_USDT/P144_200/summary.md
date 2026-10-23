# EMA Hourly Continuation — COTI/USDT P144_200

**Symbol:** COTI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.5671 |
| net_win_rate | 0.4937 |
| gross_profit_factor | 0.9791 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -3.4590 |
| sortino_ratio | -0.9689 |
| max_drawdown | 0.7220 |
| cagr | -0.3768 |
| net_avg_win | 46.4534 |
| net_avg_loss | -79.8756 |
| avg_hold_time_bars | 4.3073 |
| exposure | 0.0777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
