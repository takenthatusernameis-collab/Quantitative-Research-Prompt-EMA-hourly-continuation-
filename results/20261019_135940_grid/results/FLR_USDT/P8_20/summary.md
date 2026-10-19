# EMA Hourly Continuation — FLR/USDT P8_20

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1923 |
| net_profit_factor | 0.2969 |
| net_win_rate | 0.3869 |
| gross_profit_factor | 0.8098 |
| gross_win_rate | 0.4280 |
| sharpe_ratio | -16.4198 |
| sortino_ratio | -10.2951 |
| max_drawdown | 1.0000 |
| cagr | -0.9950 |
| net_avg_win | 5.6745 |
| net_avg_loss | -12.0626 |
| avg_hold_time_bars | 2.6604 |
| exposure | 0.2325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
