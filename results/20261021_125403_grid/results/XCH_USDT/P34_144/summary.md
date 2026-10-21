# EMA Hourly Continuation — XCH/USDT P34_144

**Symbol:** XCH/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.8355 |
| net_win_rate | 0.5071 |
| gross_profit_factor | 1.0202 |
| gross_win_rate | 0.5071 |
| sharpe_ratio | -1.0933 |
| sortino_ratio | -0.3214 |
| max_drawdown | 0.3243 |
| cagr | -0.1394 |
| net_avg_win | 74.9145 |
| net_avg_loss | -92.2618 |
| avg_hold_time_bars | 21.3238 |
| exposure | 0.4071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
