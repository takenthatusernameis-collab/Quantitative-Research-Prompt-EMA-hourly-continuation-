# EMA Hourly Continuation — ZEN/USDT P12_20

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6493 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 0.9621 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -2.3913 |
| sortino_ratio | -0.6296 |
| max_drawdown | 0.5157 |
| cagr | -0.2498 |
| net_avg_win | 57.6782 |
| net_avg_loss | -85.7195 |
| avg_hold_time_bars | 4.7530 |
| exposure | 0.0726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
