# EMA Hourly Continuation — CARV/USDT P21_100

**Symbol:** CARV/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.6078 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 0.9391 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -3.9870 |
| sortino_ratio | -1.3963 |
| max_drawdown | 0.7543 |
| cagr | -0.4851 |
| net_avg_win | 48.9902 |
| net_avg_loss | -70.6456 |
| avg_hold_time_bars | 14.9880 |
| exposure | 0.4226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
