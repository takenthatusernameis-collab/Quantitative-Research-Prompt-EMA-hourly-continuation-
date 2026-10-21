# EMA Hourly Continuation — MASK/USDT P89_100

**Symbol:** MASK/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 154 |
| net_profit_factor | 0.5497 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9279 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -2.2967 |
| sortino_ratio | -0.4105 |
| max_drawdown | 0.4093 |
| cagr | -0.1735 |
| net_avg_win | 62.7235 |
| net_avg_loss | -105.5482 |
| avg_hold_time_bars | 3.3831 |
| exposure | 0.0237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
