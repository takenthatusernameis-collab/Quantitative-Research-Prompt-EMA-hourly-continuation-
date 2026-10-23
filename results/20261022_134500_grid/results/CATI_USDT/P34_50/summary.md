# EMA Hourly Continuation — CATI/USDT P34_50

**Symbol:** CATI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 853 |
| net_profit_factor | 0.3937 |
| net_win_rate | 0.3869 |
| gross_profit_factor | 0.7646 |
| gross_win_rate | 0.4279 |
| sharpe_ratio | -10.7650 |
| sortino_ratio | -4.9227 |
| max_drawdown | 0.9946 |
| cagr | -0.9168 |
| net_avg_win | 19.5628 |
| net_avg_loss | -31.3562 |
| avg_hold_time_bars | 2.7608 |
| exposure | 0.1291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
