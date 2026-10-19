# EMA Hourly Continuation — KAS/USDT P8_26

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1584 |
| net_profit_factor | 0.3563 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.7722 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -9.5220 |
| sortino_ratio | -5.2891 |
| max_drawdown | 0.9989 |
| cagr | -0.9326 |
| net_avg_win | 7.5433 |
| net_avg_loss | -18.2348 |
| avg_hold_time_bars | 3.8403 |
| exposure | 0.2765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
