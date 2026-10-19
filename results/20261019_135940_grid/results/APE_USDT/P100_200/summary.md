# EMA Hourly Continuation — APE/USDT P100_200

**Symbol:** APE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.5141 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.8105 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -3.7609 |
| sortino_ratio | -1.1132 |
| max_drawdown | 0.7379 |
| cagr | -0.4132 |
| net_avg_win | 38.6418 |
| net_avg_loss | -63.7990 |
| avg_hold_time_bars | 7.7864 |
| exposure | 0.1557 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
