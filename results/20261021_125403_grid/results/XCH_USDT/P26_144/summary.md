# EMA Hourly Continuation — XCH/USDT P26_144

**Symbol:** XCH/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.8337 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0160 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -1.0705 |
| sortino_ratio | -0.3203 |
| max_drawdown | 0.3531 |
| cagr | -0.1392 |
| net_avg_win | 71.1392 |
| net_avg_loss | -88.1201 |
| avg_hold_time_bars | 23.3770 |
| exposure | 0.4622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
