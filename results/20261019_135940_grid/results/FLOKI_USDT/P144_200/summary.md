# EMA Hourly Continuation — FLOKI/USDT P144_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.4766 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.8593 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -4.0745 |
| sortino_ratio | -1.0757 |
| max_drawdown | 0.7441 |
| cagr | -0.4138 |
| net_avg_win | 40.5119 |
| net_avg_loss | -75.0538 |
| avg_hold_time_bars | 4.6073 |
| exposure | 0.0741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
