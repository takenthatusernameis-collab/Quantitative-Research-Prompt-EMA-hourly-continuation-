# EMA Hourly Continuation — WLD/USDT P8_12

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1896 |
| net_profit_factor | 0.2285 |
| net_win_rate | 0.3782 |
| gross_profit_factor | 0.5869 |
| gross_win_rate | 0.4051 |
| sharpe_ratio | -16.8102 |
| sortino_ratio | -10.4752 |
| max_drawdown | 1.0000 |
| cagr | -0.9961 |
| net_avg_win | 4.1297 |
| net_avg_loss | -10.9932 |
| avg_hold_time_bars | 1.6013 |
| exposure | 0.1380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
