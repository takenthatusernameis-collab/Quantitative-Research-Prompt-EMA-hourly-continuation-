# EMA Hourly Continuation — AXL/USDT P12_26

**Symbol:** AXL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1459 |
| net_profit_factor | 0.4993 |
| net_win_rate | 0.4249 |
| gross_profit_factor | 0.9531 |
| gross_win_rate | 0.4428 |
| sharpe_ratio | -10.2420 |
| sortino_ratio | -5.5173 |
| max_drawdown | 0.9989 |
| cagr | -0.9335 |
| net_avg_win | 16.0638 |
| net_avg_loss | -23.7769 |
| avg_hold_time_bars | 3.1337 |
| exposure | 0.2069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
