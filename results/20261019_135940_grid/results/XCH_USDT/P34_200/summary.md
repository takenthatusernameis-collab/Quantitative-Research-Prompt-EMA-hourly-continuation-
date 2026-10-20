# EMA Hourly Continuation — XCH/USDT P34_200

**Symbol:** XCH/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6222 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.9282 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -2.9812 |
| sortino_ratio | -0.9244 |
| max_drawdown | 0.6742 |
| cagr | -0.3579 |
| net_avg_win | 47.6599 |
| net_avg_loss | -69.9625 |
| avg_hold_time_bars | 23.5638 |
| exposure | 0.5205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
