# EMA Hourly Continuation — BLZ/USDT P89_144

**Symbol:** BLZ/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 562 |
| net_profit_factor | 0.5157 |
| net_win_rate | 0.4181 |
| gross_profit_factor | 0.8415 |
| gross_win_rate | 0.4306 |
| sharpe_ratio | -5.9422 |
| sortino_ratio | -1.9768 |
| max_drawdown | 0.9145 |
| cagr | -0.6193 |
| net_avg_win | 41.3541 |
| net_avg_loss | -57.6245 |
| avg_hold_time_bars | 6.7918 |
| exposure | 0.1727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
