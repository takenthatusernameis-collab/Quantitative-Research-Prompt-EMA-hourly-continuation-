# EMA Hourly Continuation — XCH/USDT P20_34

**Symbol:** XCH/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.5864 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8147 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -2.8940 |
| sortino_ratio | -0.7315 |
| max_drawdown | 0.5790 |
| cagr | -0.2845 |
| net_avg_win | 57.1895 |
| net_avg_loss | -79.4803 |
| avg_hold_time_bars | 5.1274 |
| exposure | 0.0732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
