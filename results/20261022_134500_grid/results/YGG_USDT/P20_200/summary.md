# EMA Hourly Continuation — YGG/USDT P20_200

**Symbol:** YGG/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.7265 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9687 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -2.2831 |
| sortino_ratio | -0.6539 |
| max_drawdown | 0.5983 |
| cagr | -0.2669 |
| net_avg_win | 72.5111 |
| net_avg_loss | -92.3753 |
| avg_hold_time_bars | 32.4034 |
| exposure | 0.6070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
