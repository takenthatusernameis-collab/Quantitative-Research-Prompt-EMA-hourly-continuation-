# EMA Hourly Continuation — FLR/USDT P8_144

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 737 |
| net_profit_factor | 0.4954 |
| net_win_rate | 0.4396 |
| gross_profit_factor | 0.8189 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -5.7608 |
| sortino_ratio | -2.1841 |
| max_drawdown | 0.9336 |
| cagr | -0.6589 |
| net_avg_win | 28.2701 |
| net_avg_loss | -44.7657 |
| avg_hold_time_bars | 19.7476 |
| exposure | 0.6615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
