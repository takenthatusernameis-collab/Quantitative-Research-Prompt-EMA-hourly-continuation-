# EMA Hourly Continuation — G/USDT P20_200

**Symbol:** G/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.6364 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.7729 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -2.3280 |
| sortino_ratio | -0.5623 |
| max_drawdown | 0.4858 |
| cagr | -0.2285 |
| net_avg_win | 67.2851 |
| net_avg_loss | -83.9823 |
| avg_hold_time_bars | 50.2253 |
| exposure | 0.6682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
