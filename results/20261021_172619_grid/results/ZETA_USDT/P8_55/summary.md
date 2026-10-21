# EMA Hourly Continuation — ZETA/USDT P8_55

**Symbol:** ZETA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.7959 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 1.0064 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -2.0826 |
| sortino_ratio | -0.7568 |
| max_drawdown | 0.6078 |
| cagr | -0.2949 |
| net_avg_win | 70.9482 |
| net_avg_loss | -88.0492 |
| avg_hold_time_bars | 17.0355 |
| exposure | 0.4995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
