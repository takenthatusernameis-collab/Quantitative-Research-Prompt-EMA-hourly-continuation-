# EMA Hourly Continuation — XYO/USDT P26_200

**Symbol:** XYO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.6626 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.8587 |
| gross_win_rate | 0.4641 |
| sharpe_ratio | -2.4642 |
| sortino_ratio | -0.6642 |
| max_drawdown | 0.5612 |
| cagr | -0.2641 |
| net_avg_win | 62.9701 |
| net_avg_loss | -82.2997 |
| avg_hold_time_bars | 33.2155 |
| exposure | 0.5441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
