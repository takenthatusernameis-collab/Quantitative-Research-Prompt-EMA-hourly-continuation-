# EMA Hourly Continuation — HNT/USDT P12_144

**Symbol:** HNT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.6129 |
| net_win_rate | 0.4544 |
| gross_profit_factor | 0.8439 |
| gross_win_rate | 0.4581 |
| sharpe_ratio | -3.6913 |
| sortino_ratio | -1.1953 |
| max_drawdown | 0.7768 |
| cagr | -0.4402 |
| net_avg_win | 49.7690 |
| net_avg_loss | -67.6273 |
| avg_hold_time_bars | 26.8790 |
| exposure | 0.6561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
