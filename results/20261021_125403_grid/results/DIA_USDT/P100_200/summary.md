# EMA Hourly Continuation — DIA/USDT P100_200

**Symbol:** DIA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.9687 |
| net_win_rate | 0.5592 |
| gross_profit_factor | 1.2544 |
| gross_win_rate | 0.5592 |
| sharpe_ratio | -0.1288 |
| sortino_ratio | -0.0326 |
| max_drawdown | 0.2631 |
| cagr | -0.0200 |
| net_avg_win | 90.1983 |
| net_avg_loss | -118.1332 |
| avg_hold_time_bars | 12.1184 |
| exposure | 0.1667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
