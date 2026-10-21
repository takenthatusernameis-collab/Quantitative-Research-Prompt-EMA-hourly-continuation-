# EMA Hourly Continuation — XCN/USDT P55_144

**Symbol:** XCN/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.7353 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9473 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -1.8556 |
| sortino_ratio | -0.4962 |
| max_drawdown | 0.4549 |
| cagr | -0.2040 |
| net_avg_win | 71.2865 |
| net_avg_loss | -91.0555 |
| avg_hold_time_bars | 14.8490 |
| exposure | 0.2369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
