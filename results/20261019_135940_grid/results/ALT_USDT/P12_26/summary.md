# EMA Hourly Continuation — ALT/USDT P12_26

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1158 |
| net_profit_factor | 0.4654 |
| net_win_rate | 0.4396 |
| gross_profit_factor | 0.8580 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -8.1927 |
| sortino_ratio | -3.9363 |
| max_drawdown | 0.9922 |
| cagr | -0.8536 |
| net_avg_win | 16.9676 |
| net_avg_loss | -28.5920 |
| avg_hold_time_bars | 4.1123 |
| exposure | 0.2165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
