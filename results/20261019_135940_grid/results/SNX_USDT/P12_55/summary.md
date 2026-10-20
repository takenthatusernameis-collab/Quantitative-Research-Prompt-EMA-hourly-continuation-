# EMA Hourly Continuation — SNX/USDT P12_55

**Symbol:** SNX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1020 |
| net_profit_factor | 0.5796 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.9852 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -5.7742 |
| sortino_ratio | -2.5813 |
| max_drawdown | 0.9589 |
| cagr | -0.7128 |
| net_avg_win | 27.6635 |
| net_avg_loss | -41.9257 |
| avg_hold_time_bars | 8.1039 |
| exposure | 0.3740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
