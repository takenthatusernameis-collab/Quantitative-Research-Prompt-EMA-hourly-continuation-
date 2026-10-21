# EMA Hourly Continuation — SAND/USDT P8_26

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6821 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9404 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -3.1353 |
| sortino_ratio | -1.1504 |
| max_drawdown | 0.7392 |
| cagr | -0.4091 |
| net_avg_win | 49.6282 |
| net_avg_loss | -67.8365 |
| avg_hold_time_bars | 7.3851 |
| exposure | 0.2205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
