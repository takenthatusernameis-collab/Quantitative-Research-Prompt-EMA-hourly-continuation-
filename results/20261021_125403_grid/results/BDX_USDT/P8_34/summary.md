# EMA Hourly Continuation — BDX/USDT P8_34

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.4338 |
| net_win_rate | 0.3675 |
| gross_profit_factor | 0.6961 |
| gross_win_rate | 0.3718 |
| sharpe_ratio | -6.6416 |
| sortino_ratio | -2.0614 |
| max_drawdown | 0.9166 |
| cagr | -0.6224 |
| net_avg_win | 40.6870 |
| net_avg_loss | -54.4993 |
| avg_hold_time_bars | 6.1667 |
| exposure | 0.1312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
