# EMA Hourly Continuation — ANKR/USDT P21_34

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1110 |
| net_profit_factor | 0.3647 |
| net_win_rate | 0.4009 |
| gross_profit_factor | 0.8363 |
| gross_win_rate | 0.4306 |
| sharpe_ratio | -11.6251 |
| sortino_ratio | -5.5460 |
| max_drawdown | 0.9993 |
| cagr | -0.9421 |
| net_avg_win | 12.8897 |
| net_avg_loss | -23.6513 |
| avg_hold_time_bars | 4.1495 |
| exposure | 0.2094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
