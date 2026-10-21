# EMA Hourly Continuation — ETC/USDT P12_20

**Symbol:** ETC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.6028 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 0.9933 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -2.5172 |
| sortino_ratio | -0.6317 |
| max_drawdown | 0.5231 |
| cagr | -0.2491 |
| net_avg_win | 50.8812 |
| net_avg_loss | -86.6732 |
| avg_hold_time_bars | 4.4636 |
| exposure | 0.0613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
