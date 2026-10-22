# EMA Hourly Continuation — XCH/USDT P12_200

**Symbol:** XCH/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.9548 |
| net_win_rate | 0.5330 |
| gross_profit_factor | 1.1302 |
| gross_win_rate | 0.5330 |
| sharpe_ratio | -0.2246 |
| sortino_ratio | -0.0618 |
| max_drawdown | 0.1740 |
| cagr | -0.0338 |
| net_avg_win | 90.1224 |
| net_avg_loss | -107.7164 |
| avg_hold_time_bars | 43.3104 |
| exposure | 0.7166 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
