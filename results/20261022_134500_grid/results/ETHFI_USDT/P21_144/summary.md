# EMA Hourly Continuation — ETHFI/USDT P21_144

**Symbol:** ETHFI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.7754 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 1.0145 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -2.2501 |
| sortino_ratio | -0.7473 |
| max_drawdown | 0.6091 |
| cagr | -0.2954 |
| net_avg_win | 75.0622 |
| net_avg_loss | -93.0038 |
| avg_hold_time_bars | 20.6958 |
| exposure | 0.5165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
