# EMA Hourly Continuation — CAKE/USDT P50_200

**Symbol:** CAKE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.6982 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.8925 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -1.6749 |
| sortino_ratio | -0.3909 |
| max_drawdown | 0.4272 |
| cagr | -0.1649 |
| net_avg_win | 64.7645 |
| net_avg_loss | -86.7510 |
| avg_hold_time_bars | 30.3866 |
| exposure | 0.3715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
