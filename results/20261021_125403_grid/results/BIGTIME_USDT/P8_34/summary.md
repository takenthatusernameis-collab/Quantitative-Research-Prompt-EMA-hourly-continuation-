# EMA Hourly Continuation — BIGTIME/USDT P8_34

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 741 |
| net_profit_factor | 0.7112 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9106 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -3.0906 |
| sortino_ratio | -1.1979 |
| max_drawdown | 0.7626 |
| cagr | -0.4228 |
| net_avg_win | 52.0234 |
| net_avg_loss | -67.2752 |
| avg_hold_time_bars | 9.7800 |
| exposure | 0.3279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
