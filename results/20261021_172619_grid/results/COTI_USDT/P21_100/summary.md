# EMA Hourly Continuation — COTI/USDT P21_100

**Symbol:** COTI/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.8397 |
| net_win_rate | 0.5049 |
| gross_profit_factor | 1.0207 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -1.2676 |
| sortino_ratio | -0.4092 |
| max_drawdown | 0.4502 |
| cagr | -0.1735 |
| net_avg_win | 77.8079 |
| net_avg_loss | -94.5109 |
| avg_hold_time_bars | 16.6785 |
| exposure | 0.3844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
