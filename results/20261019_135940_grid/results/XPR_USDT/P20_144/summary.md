# EMA Hourly Continuation — XPR/USDT P20_144

**Symbol:** XPR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.5066 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.7807 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -4.3341 |
| sortino_ratio | -1.4270 |
| max_drawdown | 0.8254 |
| cagr | -0.4925 |
| net_avg_win | 34.0036 |
| net_avg_loss | -55.6322 |
| avg_hold_time_bars | 19.4789 |
| exposure | 0.4825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
