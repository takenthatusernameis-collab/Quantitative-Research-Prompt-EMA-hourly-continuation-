# EMA Hourly Continuation — SHIB/USDT P144_200

**Symbol:** SHIB/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.4322 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.9623 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -5.2943 |
| sortino_ratio | -1.4662 |
| max_drawdown | 0.8543 |
| cagr | -0.5339 |
| net_avg_win | 36.0732 |
| net_avg_loss | -71.8799 |
| avg_hold_time_bars | 4.0129 |
| exposure | 0.0710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
