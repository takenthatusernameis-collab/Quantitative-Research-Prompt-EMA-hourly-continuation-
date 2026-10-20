# EMA Hourly Continuation — XCH/USDT P12_100

**Symbol:** XCH/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 787 |
| net_profit_factor | 0.6211 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9533 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -3.9369 |
| sortino_ratio | -1.5643 |
| max_drawdown | 0.8446 |
| cagr | -0.5201 |
| net_avg_win | 37.1000 |
| net_avg_loss | -53.5404 |
| avg_hold_time_bars | 16.4790 |
| exposure | 0.5895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
