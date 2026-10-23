# EMA Hourly Continuation — ZRX/USDT P12_50

**Symbol:** ZRX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1040 |
| net_profit_factor | 0.5310 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.8905 |
| gross_win_rate | 0.4702 |
| sharpe_ratio | -6.4326 |
| sortino_ratio | -2.9167 |
| max_drawdown | 0.9718 |
| cagr | -0.7554 |
| net_avg_win | 23.1888 |
| net_avg_loss | -36.5730 |
| avg_hold_time_bars | 7.7885 |
| exposure | 0.3682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
