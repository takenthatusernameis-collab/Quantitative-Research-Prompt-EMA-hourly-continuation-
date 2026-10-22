# EMA Hourly Continuation — GRT/USDT P12_50

**Symbol:** GRT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1077 |
| net_profit_factor | 0.6089 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.9701 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -6.4093 |
| sortino_ratio | -2.9511 |
| max_drawdown | 0.9746 |
| cagr | -0.7617 |
| net_avg_win | 30.4209 |
| net_avg_loss | -42.9730 |
| avg_hold_time_bars | 7.0520 |
| exposure | 0.3437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
