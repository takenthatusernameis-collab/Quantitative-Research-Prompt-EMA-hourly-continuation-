# EMA Hourly Continuation — YGG/USDT P12_50

**Symbol:** YGG/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.5873 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8784 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -6.2560 |
| sortino_ratio | -2.8502 |
| max_drawdown | 0.9686 |
| cagr | -0.7457 |
| net_avg_win | 28.8855 |
| net_avg_loss | -40.3825 |
| avg_hold_time_bars | 7.3015 |
| exposure | 0.3496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
