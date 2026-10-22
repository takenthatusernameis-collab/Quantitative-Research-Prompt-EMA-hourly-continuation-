# EMA Hourly Continuation — SUI/USDT P34_100

**Symbol:** SUI/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.6269 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9760 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -4.3891 |
| sortino_ratio | -1.6072 |
| max_drawdown | 0.8683 |
| cagr | -0.5435 |
| net_avg_win | 44.3435 |
| net_avg_loss | -65.1418 |
| avg_hold_time_bars | 7.9515 |
| exposure | 0.2458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
