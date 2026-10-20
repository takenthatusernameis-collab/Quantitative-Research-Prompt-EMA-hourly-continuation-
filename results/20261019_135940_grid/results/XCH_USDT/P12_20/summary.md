# EMA Hourly Continuation — XCH/USDT P12_20

**Symbol:** XCH/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1728 |
| net_profit_factor | 0.1556 |
| net_win_rate | 0.3594 |
| gross_profit_factor | 0.6531 |
| gross_win_rate | 0.3929 |
| sharpe_ratio | -16.6235 |
| sortino_ratio | -9.9519 |
| max_drawdown | 1.0000 |
| cagr | -0.9943 |
| net_avg_win | 2.9663 |
| net_avg_loss | -10.6974 |
| avg_hold_time_bars | 2.0926 |
| exposure | 0.1644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
