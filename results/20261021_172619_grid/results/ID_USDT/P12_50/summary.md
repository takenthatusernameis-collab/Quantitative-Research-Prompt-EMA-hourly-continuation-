# EMA Hourly Continuation — ID/USDT P12_50

**Symbol:** ID/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.7243 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 0.9643 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -2.6283 |
| sortino_ratio | -0.9741 |
| max_drawdown | 0.6991 |
| cagr | -0.3603 |
| net_avg_win | 53.6582 |
| net_avg_loss | -71.4868 |
| avg_hold_time_bars | 11.2611 |
| exposure | 0.3435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
