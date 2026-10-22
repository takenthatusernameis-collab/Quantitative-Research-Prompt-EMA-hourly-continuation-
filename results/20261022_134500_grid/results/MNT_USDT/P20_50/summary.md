# EMA Hourly Continuation — MNT/USDT P20_50

**Symbol:** MNT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.3438 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 0.7740 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -8.8122 |
| sortino_ratio | -3.7805 |
| max_drawdown | 0.9925 |
| cagr | -0.8551 |
| net_avg_win | 12.9010 |
| net_avg_loss | -29.0227 |
| avg_hold_time_bars | 5.8766 |
| exposure | 0.2468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
