# EMA Hourly Continuation — ZETA/USDT P12_20

**Symbol:** ZETA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.6955 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 1.0038 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -2.5949 |
| sortino_ratio | -0.7731 |
| max_drawdown | 0.6145 |
| cagr | -0.2972 |
| net_avg_win | 62.8925 |
| net_avg_loss | -88.3603 |
| avg_hold_time_bars | 4.7529 |
| exposure | 0.0931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
