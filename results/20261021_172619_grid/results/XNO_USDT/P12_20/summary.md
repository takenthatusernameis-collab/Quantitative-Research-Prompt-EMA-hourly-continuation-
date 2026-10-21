# EMA Hourly Continuation — XNO/USDT P12_20

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.5146 |
| net_win_rate | 0.4034 |
| gross_profit_factor | 0.7369 |
| gross_win_rate | 0.4034 |
| sharpe_ratio | -4.3239 |
| sortino_ratio | -1.1625 |
| max_drawdown | 0.7421 |
| cagr | -0.4167 |
| net_avg_win | 54.6144 |
| net_avg_loss | -71.7454 |
| avg_hold_time_bars | 4.4482 |
| exposure | 0.0722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
