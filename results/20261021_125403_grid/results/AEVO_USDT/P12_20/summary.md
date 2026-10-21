# EMA Hourly Continuation — AEVO/USDT P12_20

**Symbol:** AEVO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.6153 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8547 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -3.3300 |
| sortino_ratio | -0.9876 |
| max_drawdown | 0.6881 |
| cagr | -0.3638 |
| net_avg_win | 54.6930 |
| net_avg_loss | -75.5924 |
| avg_hold_time_bars | 5.3995 |
| exposure | 0.1058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
