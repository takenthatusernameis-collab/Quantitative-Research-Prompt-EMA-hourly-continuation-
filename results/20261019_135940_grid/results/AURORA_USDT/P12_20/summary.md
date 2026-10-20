# EMA Hourly Continuation — AURORA/USDT P12_20

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1233 |
| net_profit_factor | 0.2758 |
| net_win_rate | 0.3131 |
| gross_profit_factor | 0.7359 |
| gross_win_rate | 0.3674 |
| sharpe_ratio | -16.2558 |
| sortino_ratio | -8.3692 |
| max_drawdown | 1.0000 |
| cagr | -0.9894 |
| net_avg_win | 9.8679 |
| net_avg_loss | -16.3033 |
| avg_hold_time_bars | 3.1379 |
| exposure | 0.1759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
