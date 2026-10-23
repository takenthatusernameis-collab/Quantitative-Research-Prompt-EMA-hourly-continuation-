# EMA Hourly Continuation — KSM/USDT P12_100

**Symbol:** KSM/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.5649 |
| net_win_rate | 0.4319 |
| gross_profit_factor | 0.8631 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -4.9135 |
| sortino_ratio | -1.7072 |
| max_drawdown | 0.8740 |
| cagr | -0.5552 |
| net_avg_win | 42.9085 |
| net_avg_loss | -57.7382 |
| avg_hold_time_bars | 22.1560 |
| exposure | 0.6133 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
