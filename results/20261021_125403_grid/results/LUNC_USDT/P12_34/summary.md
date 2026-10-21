# EMA Hourly Continuation — LUNC/USDT P12_34

**Symbol:** LUNC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.5771 |
| net_win_rate | 0.4371 |
| gross_profit_factor | 0.7953 |
| gross_win_rate | 0.4371 |
| sharpe_ratio | -4.2522 |
| sortino_ratio | -1.4280 |
| max_drawdown | 0.8094 |
| cagr | -0.4818 |
| net_avg_win | 45.3791 |
| net_avg_loss | -61.0504 |
| avg_hold_time_bars | 6.3435 |
| exposure | 0.1603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
