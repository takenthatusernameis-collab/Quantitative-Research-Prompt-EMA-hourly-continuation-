# EMA Hourly Continuation — OP/USDT P8_34

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1349 |
| net_profit_factor | 0.4730 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -7.7905 |
| sortino_ratio | -4.0055 |
| max_drawdown | 0.9931 |
| cagr | -0.8619 |
| net_avg_win | 14.2848 |
| net_avg_loss | -25.9923 |
| avg_hold_time_bars | 5.7035 |
| exposure | 0.3497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
