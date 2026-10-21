# EMA Hourly Continuation — XCN/USDT P20_144

**Symbol:** XCN/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.6853 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.8378 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -2.4979 |
| sortino_ratio | -0.7348 |
| max_drawdown | 0.5726 |
| cagr | -0.2871 |
| net_avg_win | 63.6034 |
| net_avg_loss | -77.4106 |
| avg_hold_time_bars | 25.5615 |
| exposure | 0.5008 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
