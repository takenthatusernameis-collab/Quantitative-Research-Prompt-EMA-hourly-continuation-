# EMA Hourly Continuation — NUM/USDT P8_26

**Symbol:** NUM/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1409 |
| net_profit_factor | 0.3619 |
| net_win_rate | 0.3407 |
| gross_profit_factor | 0.7435 |
| gross_win_rate | 0.3591 |
| sharpe_ratio | -14.0194 |
| sortino_ratio | -7.4436 |
| max_drawdown | 0.9999 |
| cagr | -0.9771 |
| net_avg_win | 11.8137 |
| net_avg_loss | -16.8674 |
| avg_hold_time_bars | 4.4855 |
| exposure | 0.2873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
