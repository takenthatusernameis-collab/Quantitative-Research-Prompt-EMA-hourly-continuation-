# EMA Hourly Continuation — SEI/USDT P34_200

**Symbol:** SEI/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7779 |
| net_win_rate | 0.5150 |
| gross_profit_factor | 1.0702 |
| gross_win_rate | 0.5210 |
| sharpe_ratio | -1.3592 |
| sortino_ratio | -0.3507 |
| max_drawdown | 0.3864 |
| cagr | -0.1539 |
| net_avg_win | 69.7901 |
| net_avg_loss | -95.2540 |
| avg_hold_time_bars | 35.1796 |
| exposure | 0.5341 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
