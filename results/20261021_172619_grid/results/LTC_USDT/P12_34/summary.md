# EMA Hourly Continuation — LTC/USDT P12_34

**Symbol:** LTC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6942 |
| net_win_rate | 0.5082 |
| gross_profit_factor | 1.0548 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -2.6769 |
| sortino_ratio | -0.8505 |
| max_drawdown | 0.6229 |
| cagr | -0.3196 |
| net_avg_win | 56.9616 |
| net_avg_loss | -84.7987 |
| avg_hold_time_bars | 6.9342 |
| exposure | 0.1532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
