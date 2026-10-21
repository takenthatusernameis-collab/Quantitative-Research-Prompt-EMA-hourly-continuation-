# EMA Hourly Continuation — NMR/USDT P20_21

**Symbol:** NMR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.6732 |
| net_win_rate | 0.5085 |
| gross_profit_factor | 1.0847 |
| gross_win_rate | 0.5171 |
| sharpe_ratio | -1.9919 |
| sortino_ratio | -0.4391 |
| max_drawdown | 0.4370 |
| cagr | -0.1808 |
| net_avg_win | 68.2028 |
| net_avg_loss | -104.8290 |
| avg_hold_time_bars | 5.1068 |
| exposure | 0.0543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
