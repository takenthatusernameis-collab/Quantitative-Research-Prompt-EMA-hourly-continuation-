# EMA Hourly Continuation — ALPINE/USDT P26_144

**Symbol:** ALPINE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.6593 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 1.0068 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -3.4494 |
| sortino_ratio | -1.0964 |
| max_drawdown | 0.7530 |
| cagr | -0.4135 |
| net_avg_win | 57.3572 |
| net_avg_loss | -80.5343 |
| avg_hold_time_bars | 21.3822 |
| exposure | 0.5035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
