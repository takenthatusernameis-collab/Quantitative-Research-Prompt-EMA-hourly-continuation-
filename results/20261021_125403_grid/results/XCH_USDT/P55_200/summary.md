# EMA Hourly Continuation — XCH/USDT P55_200

**Symbol:** XCH/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.8411 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0223 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -0.9466 |
| sortino_ratio | -0.2413 |
| max_drawdown | 0.2471 |
| cagr | -0.1069 |
| net_avg_win | 81.7484 |
| net_avg_loss | -99.6865 |
| avg_hold_time_bars | 24.3671 |
| exposure | 0.3500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
