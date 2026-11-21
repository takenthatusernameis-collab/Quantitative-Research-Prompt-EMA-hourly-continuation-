# EMA Hourly Continuation — HTR/USDT P12_20

**Symbol:** HTR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1305 |
| net_profit_factor | 0.2848 |
| net_win_rate | 0.3349 |
| gross_profit_factor | 0.6163 |
| gross_win_rate | 0.3609 |
| sharpe_ratio | -13.9827 |
| sortino_ratio | -7.1934 |
| max_drawdown | 0.9999 |
| cagr | -0.9755 |
| net_avg_win | 9.1137 |
| net_avg_loss | -16.1080 |
| avg_hold_time_bars | 2.9678 |
| exposure | 0.1760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
