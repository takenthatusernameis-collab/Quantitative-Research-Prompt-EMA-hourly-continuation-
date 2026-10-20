# EMA Hourly Continuation — ANYONE/USDT P20_34

**Symbol:** ANYONE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 976 |
| net_profit_factor | 0.3912 |
| net_win_rate | 0.3842 |
| gross_profit_factor | 0.6485 |
| gross_win_rate | 0.3904 |
| sharpe_ratio | -9.5394 |
| sortino_ratio | -4.4411 |
| max_drawdown | 0.9926 |
| cagr | -0.8859 |
| net_avg_win | 17.0065 |
| net_avg_loss | -27.1269 |
| avg_hold_time_bars | 3.1670 |
| exposure | 0.1562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
