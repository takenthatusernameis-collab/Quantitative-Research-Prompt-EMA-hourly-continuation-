# EMA Hourly Continuation — API3/USDT P12_34

**Symbol:** API3/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1280 |
| net_profit_factor | 0.5254 |
| net_win_rate | 0.4352 |
| gross_profit_factor | 0.8912 |
| gross_win_rate | 0.4461 |
| sharpe_ratio | -8.8398 |
| sortino_ratio | -4.4674 |
| max_drawdown | 0.9957 |
| cagr | -0.8853 |
| net_avg_win | 19.7883 |
| net_avg_loss | -29.0160 |
| avg_hold_time_bars | 4.6750 |
| exposure | 0.2720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
