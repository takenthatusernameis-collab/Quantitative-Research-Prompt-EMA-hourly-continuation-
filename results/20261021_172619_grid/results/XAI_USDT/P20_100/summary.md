# EMA Hourly Continuation — XAI/USDT P20_100

**Symbol:** XAI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7448 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8985 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -2.4179 |
| sortino_ratio | -0.7493 |
| max_drawdown | 0.6589 |
| cagr | -0.2921 |
| net_avg_win | 76.9228 |
| net_avg_loss | -88.7604 |
| avg_hold_time_bars | 22.5147 |
| exposure | 0.4871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
