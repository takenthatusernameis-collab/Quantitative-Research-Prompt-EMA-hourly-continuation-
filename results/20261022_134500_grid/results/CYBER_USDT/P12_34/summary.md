# EMA Hourly Continuation — CYBER/USDT P12_34

**Symbol:** CYBER/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1221 |
| net_profit_factor | 0.4983 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.8636 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -8.1065 |
| sortino_ratio | -3.9979 |
| max_drawdown | 0.9929 |
| cagr | -0.8587 |
| net_avg_win | 17.9569 |
| net_avg_loss | -29.4418 |
| avg_hold_time_bars | 4.8460 |
| exposure | 0.2690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
