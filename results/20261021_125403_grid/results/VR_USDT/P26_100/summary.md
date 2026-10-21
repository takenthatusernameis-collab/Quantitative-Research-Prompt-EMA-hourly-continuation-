# EMA Hourly Continuation — VR/USDT P26_100

**Symbol:** VR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.6326 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.7865 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -2.5885 |
| sortino_ratio | -0.6810 |
| max_drawdown | 0.5504 |
| cagr | -0.2701 |
| net_avg_win | 61.0977 |
| net_avg_loss | -77.4692 |
| avg_hold_time_bars | 20.1705 |
| exposure | 0.3172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
