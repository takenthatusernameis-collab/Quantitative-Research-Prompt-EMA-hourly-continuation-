# EMA Hourly Continuation — XCN/USDT P89_144

**Symbol:** XCN/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.3461 |
| net_win_rate | 0.3888 |
| gross_profit_factor | 0.7106 |
| gross_win_rate | 0.4070 |
| sharpe_ratio | -8.1051 |
| sortino_ratio | -2.9601 |
| max_drawdown | 0.9766 |
| cagr | -0.7717 |
| net_avg_win | 20.0909 |
| net_avg_loss | -36.9266 |
| avg_hold_time_bars | 4.8169 |
| exposure | 0.1447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
