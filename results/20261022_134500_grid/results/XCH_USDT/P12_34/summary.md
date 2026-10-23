# EMA Hourly Continuation — XCH/USDT P12_34

**Symbol:** XCH/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1525 |
| net_profit_factor | 0.3047 |
| net_win_rate | 0.4249 |
| gross_profit_factor | 0.7379 |
| gross_win_rate | 0.4393 |
| sharpe_ratio | -10.8806 |
| sortino_ratio | -6.0051 |
| max_drawdown | 0.9994 |
| cagr | -0.9493 |
| net_avg_win | 6.7587 |
| net_avg_loss | -16.3900 |
| avg_hold_time_bars | 3.7207 |
| exposure | 0.2579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
