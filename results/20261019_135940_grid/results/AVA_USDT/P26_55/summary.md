# EMA Hourly Continuation — AVA/USDT P26_55

**Symbol:** AVA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 893 |
| net_profit_factor | 0.3971 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.7960 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -7.3404 |
| sortino_ratio | -3.0861 |
| max_drawdown | 0.9801 |
| cagr | -0.7839 |
| net_avg_win | 16.0774 |
| net_avg_loss | -32.9953 |
| avg_hold_time_bars | 4.2228 |
| exposure | 0.1714 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
