# EMA Hourly Continuation — XCH/USDT P50_55

**Symbol:** XCH/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 933 |
| net_profit_factor | 0.1590 |
| net_win_rate | 0.3140 |
| gross_profit_factor | 0.6261 |
| gross_win_rate | 0.3644 |
| sharpe_ratio | -14.2327 |
| sortino_ratio | -6.4399 |
| max_drawdown | 0.9999 |
| cagr | -0.9700 |
| net_avg_win | 6.4506 |
| net_avg_loss | -18.5758 |
| avg_hold_time_bars | 1.9989 |
| exposure | 0.0848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
