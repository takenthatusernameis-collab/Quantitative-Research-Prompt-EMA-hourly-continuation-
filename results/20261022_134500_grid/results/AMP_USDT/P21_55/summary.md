# EMA Hourly Continuation — AMP/USDT P21_55

**Symbol:** AMP/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1343 |
| net_profit_factor | 0.3361 |
| net_win_rate | 0.3701 |
| gross_profit_factor | 0.6756 |
| gross_win_rate | 0.3902 |
| sharpe_ratio | -12.8317 |
| sortino_ratio | -6.6858 |
| max_drawdown | 0.9998 |
| cagr | -0.9650 |
| net_avg_win | 10.1831 |
| net_avg_loss | -17.8000 |
| avg_hold_time_bars | 4.3641 |
| exposure | 0.2664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
