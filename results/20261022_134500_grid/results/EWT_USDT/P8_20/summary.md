# EMA Hourly Continuation — EWT/USDT P8_20

**Symbol:** EWT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1492 |
| net_profit_factor | 0.3003 |
| net_win_rate | 0.3472 |
| gross_profit_factor | 0.6256 |
| gross_win_rate | 0.3787 |
| sharpe_ratio | -15.4493 |
| sortino_ratio | -8.4990 |
| max_drawdown | 1.0000 |
| cagr | -0.9892 |
| net_avg_win | 8.2842 |
| net_avg_loss | -14.6726 |
| avg_hold_time_bars | 3.0965 |
| exposure | 0.2100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
