# EMA Hourly Continuation — FLR/USDT P12_50

**Symbol:** FLR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1213 |
| net_profit_factor | 0.4746 |
| net_win_rate | 0.4542 |
| gross_profit_factor | 0.8854 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -8.5616 |
| sortino_ratio | -4.1766 |
| max_drawdown | 0.9950 |
| cagr | -0.8771 |
| net_avg_win | 16.3107 |
| net_avg_loss | -28.6035 |
| avg_hold_time_bars | 6.5161 |
| exposure | 0.3593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
