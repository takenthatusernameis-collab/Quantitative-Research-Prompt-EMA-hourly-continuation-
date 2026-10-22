# EMA Hourly Continuation — IMX/USDT P26_55

**Symbol:** IMX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 910 |
| net_profit_factor | 0.5375 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.8970 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -5.5257 |
| sortino_ratio | -2.3417 |
| max_drawdown | 0.9453 |
| cagr | -0.6788 |
| net_avg_win | 25.1410 |
| net_avg_loss | -43.0202 |
| avg_hold_time_bars | 4.2033 |
| exposure | 0.1731 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
