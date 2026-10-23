# EMA Hourly Continuation — XCH/USDT P26_144

**Symbol:** XCH/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.5583 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.8977 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -4.1152 |
| sortino_ratio | -1.4135 |
| max_drawdown | 0.8287 |
| cagr | -0.5036 |
| net_avg_win | 36.9763 |
| net_avg_loss | -56.9674 |
| avg_hold_time_bars | 17.1242 |
| exposure | 0.4764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
