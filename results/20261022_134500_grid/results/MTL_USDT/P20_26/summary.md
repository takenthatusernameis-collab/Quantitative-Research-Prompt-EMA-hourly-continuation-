# EMA Hourly Continuation — MTL/USDT P20_26

**Symbol:** MTL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1132 |
| net_profit_factor | 0.2269 |
| net_win_rate | 0.3445 |
| gross_profit_factor | 0.7760 |
| gross_win_rate | 0.4143 |
| sharpe_ratio | -14.5607 |
| sortino_ratio | -7.1391 |
| max_drawdown | 0.9999 |
| cagr | -0.9768 |
| net_avg_win | 7.5253 |
| net_avg_loss | -17.4314 |
| avg_hold_time_bars | 2.9231 |
| exposure | 0.1497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
