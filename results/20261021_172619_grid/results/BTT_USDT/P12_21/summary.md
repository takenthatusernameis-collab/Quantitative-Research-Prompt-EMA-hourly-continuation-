# EMA Hourly Continuation — BTT/USDT P12_21

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.4250 |
| net_win_rate | 0.4234 |
| gross_profit_factor | 0.8049 |
| gross_win_rate | 0.4234 |
| sharpe_ratio | -5.4546 |
| sortino_ratio | -1.4497 |
| max_drawdown | 0.8229 |
| cagr | -0.4962 |
| net_avg_win | 43.0577 |
| net_avg_loss | -74.3936 |
| avg_hold_time_bars | 5.9099 |
| exposure | 0.0895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
