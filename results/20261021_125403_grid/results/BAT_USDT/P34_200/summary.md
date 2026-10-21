# EMA Hourly Continuation — BAT/USDT P34_200

**Symbol:** BAT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7645 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9443 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -1.3973 |
| sortino_ratio | -0.3487 |
| max_drawdown | 0.3756 |
| cagr | -0.1489 |
| net_avg_win | 72.5278 |
| net_avg_loss | -90.0413 |
| avg_hold_time_bars | 37.4837 |
| exposure | 0.5214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
