# EMA Hourly Continuation — CWEB/USDT P12_20

**Symbol:** CWEB/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1438 |
| net_profit_factor | 0.1899 |
| net_win_rate | 0.2128 |
| gross_profit_factor | 0.6286 |
| gross_win_rate | 0.2594 |
| sharpe_ratio | -22.1511 |
| sortino_ratio | -13.0089 |
| max_drawdown | 1.0000 |
| cagr | -0.9994 |
| net_avg_win | 7.6617 |
| net_avg_loss | -10.9050 |
| avg_hold_time_bars | 3.3999 |
| exposure | 0.2222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
