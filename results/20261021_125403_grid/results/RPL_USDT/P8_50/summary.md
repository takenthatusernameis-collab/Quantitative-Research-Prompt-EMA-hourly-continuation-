# EMA Hourly Continuation — RPL/USDT P8_50

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.8351 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0612 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -1.7430 |
| sortino_ratio | -0.6724 |
| max_drawdown | 0.5872 |
| cagr | -0.2682 |
| net_avg_win | 74.4050 |
| net_avg_loss | -92.8488 |
| avg_hold_time_bars | 14.5048 |
| exposure | 0.4772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
