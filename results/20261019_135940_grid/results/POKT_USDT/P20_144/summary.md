# EMA Hourly Continuation — POKT/USDT P20_144

**Symbol:** POKT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.5304 |
| net_win_rate | 0.3925 |
| gross_profit_factor | 0.7584 |
| gross_win_rate | 0.4008 |
| sharpe_ratio | -6.3525 |
| sortino_ratio | -2.3865 |
| max_drawdown | 0.9447 |
| cagr | -0.6813 |
| net_avg_win | 37.6794 |
| net_avg_loss | -45.9005 |
| avg_hold_time_bars | 15.6255 |
| exposure | 0.5098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
