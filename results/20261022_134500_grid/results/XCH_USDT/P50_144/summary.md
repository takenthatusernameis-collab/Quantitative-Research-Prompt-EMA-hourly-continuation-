# EMA Hourly Continuation — XCH/USDT P50_144

**Symbol:** XCH/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.5431 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.9145 |
| gross_win_rate | 0.4671 |
| sharpe_ratio | -4.4957 |
| sortino_ratio | -1.5151 |
| max_drawdown | 0.8445 |
| cagr | -0.5234 |
| net_avg_win | 38.3111 |
| net_avg_loss | -58.4895 |
| avg_hold_time_bars | 11.2093 |
| exposure | 0.2945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
