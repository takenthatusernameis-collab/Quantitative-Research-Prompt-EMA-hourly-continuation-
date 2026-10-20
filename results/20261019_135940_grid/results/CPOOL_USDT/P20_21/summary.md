# EMA Hourly Continuation — CPOOL/USDT P20_21

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1168 |
| net_profit_factor | 0.2084 |
| net_win_rate | 0.3373 |
| gross_profit_factor | 0.5778 |
| gross_win_rate | 0.3801 |
| sharpe_ratio | -15.2587 |
| sortino_ratio | -7.5931 |
| max_drawdown | 1.0000 |
| cagr | -0.9862 |
| net_avg_win | 6.6834 |
| net_avg_loss | -16.3218 |
| avg_hold_time_bars | 1.7654 |
| exposure | 0.0937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
