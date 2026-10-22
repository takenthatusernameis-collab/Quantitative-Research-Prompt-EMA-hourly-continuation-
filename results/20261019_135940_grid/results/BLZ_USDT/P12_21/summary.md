# EMA Hourly Continuation — BLZ/USDT P12_21

**Symbol:** BLZ/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1451 |
| net_profit_factor | 0.3226 |
| net_win_rate | 0.3632 |
| gross_profit_factor | 0.8560 |
| gross_win_rate | 0.4004 |
| sharpe_ratio | -14.2237 |
| sortino_ratio | -7.7157 |
| max_drawdown | 1.0000 |
| cagr | -0.9804 |
| net_avg_win | 9.0381 |
| net_avg_loss | -15.9768 |
| avg_hold_time_bars | 3.2164 |
| exposure | 0.2112 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
