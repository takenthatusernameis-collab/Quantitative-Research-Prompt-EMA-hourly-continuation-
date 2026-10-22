# EMA Hourly Continuation — DCR/USDT P20_26

**Symbol:** DCR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1249 |
| net_profit_factor | 0.2261 |
| net_win_rate | 0.3491 |
| gross_profit_factor | 0.6402 |
| gross_win_rate | 0.4043 |
| sharpe_ratio | -14.6690 |
| sortino_ratio | -7.4961 |
| max_drawdown | 1.0000 |
| cagr | -0.9810 |
| net_avg_win | 6.7006 |
| net_avg_loss | -15.8930 |
| avg_hold_time_bars | 2.4916 |
| exposure | 0.1408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
