# EMA Hourly Continuation — AURORA/USDT P12_55

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 875 |
| net_profit_factor | 0.4957 |
| net_win_rate | 0.4206 |
| gross_profit_factor | 0.8613 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -7.5520 |
| sortino_ratio | -3.1441 |
| max_drawdown | 0.9805 |
| cagr | -0.7891 |
| net_avg_win | 26.1734 |
| net_avg_loss | -38.3256 |
| avg_hold_time_bars | 9.3566 |
| exposure | 0.3721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
