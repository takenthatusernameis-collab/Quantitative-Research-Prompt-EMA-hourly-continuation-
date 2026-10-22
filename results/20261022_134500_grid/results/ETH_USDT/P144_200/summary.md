# EMA Hourly Continuation — ETH/USDT P144_200

**Symbol:** ETH/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.3890 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.8741 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -5.5850 |
| sortino_ratio | -1.5787 |
| max_drawdown | 0.8654 |
| cagr | -0.5485 |
| net_avg_win | 30.7329 |
| net_avg_loss | -65.1776 |
| avg_hold_time_bars | 4.9722 |
| exposure | 0.0895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
