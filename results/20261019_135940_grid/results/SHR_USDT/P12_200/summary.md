# EMA Hourly Continuation — SHR/USDT P12_200

**Symbol:** SHR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 793 |
| net_profit_factor | 0.4847 |
| net_win_rate | 0.3569 |
| gross_profit_factor | 0.6105 |
| gross_win_rate | 0.3569 |
| sharpe_ratio | -7.0798 |
| sortino_ratio | -2.7683 |
| max_drawdown | 0.9659 |
| cagr | -0.7337 |
| net_avg_win | 32.0551 |
| net_avg_loss | -36.6992 |
| avg_hold_time_bars | 16.6166 |
| exposure | 0.5963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
