# EMA Hourly Continuation — XNO/USDT P20_26

**Symbol:** XNO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1347 |
| net_profit_factor | 0.2055 |
| net_win_rate | 0.3044 |
| gross_profit_factor | 0.6435 |
| gross_win_rate | 0.3497 |
| sharpe_ratio | -17.1601 |
| sortino_ratio | -9.2443 |
| max_drawdown | 1.0000 |
| cagr | -0.9927 |
| net_avg_win | 6.3079 |
| net_avg_loss | -13.4324 |
| avg_hold_time_bars | 1.9436 |
| exposure | 0.1190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
