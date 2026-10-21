# EMA Hourly Continuation — FET/USDT P50_200

**Symbol:** FET/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.8986 |
| net_win_rate | 0.5136 |
| gross_profit_factor | 1.0398 |
| gross_win_rate | 0.5136 |
| sharpe_ratio | -0.4946 |
| sortino_ratio | -0.1137 |
| max_drawdown | 0.1835 |
| cagr | -0.0536 |
| net_avg_win | 86.6755 |
| net_avg_loss | -101.8596 |
| avg_hold_time_bars | 33.5914 |
| exposure | 0.3924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
