# EMA Hourly Continuation — DOT/USDT P20_200

**Symbol:** DOT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.7386 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0679 |
| gross_win_rate | 0.5184 |
| sharpe_ratio | -1.5362 |
| sortino_ratio | -0.3741 |
| max_drawdown | 0.4243 |
| cagr | -0.1649 |
| net_avg_win | 67.2450 |
| net_avg_loss | -95.4029 |
| avg_hold_time_bars | 50.6589 |
| exposure | 0.6885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
