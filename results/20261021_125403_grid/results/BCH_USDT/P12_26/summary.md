# EMA Hourly Continuation — BCH/USDT P12_26

**Symbol:** BCH/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.6407 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 0.9747 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -2.5048 |
| sortino_ratio | -0.7033 |
| max_drawdown | 0.5657 |
| cagr | -0.2736 |
| net_avg_win | 51.5418 |
| net_avg_loss | -81.2918 |
| avg_hold_time_bars | 5.9474 |
| exposure | 0.1027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
