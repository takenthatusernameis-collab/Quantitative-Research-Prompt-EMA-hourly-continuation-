# EMA Hourly Continuation — AXS/USDT P12_20

**Symbol:** AXS/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1410 |
| net_profit_factor | 0.1800 |
| net_win_rate | 0.3950 |
| gross_profit_factor | 0.5712 |
| gross_win_rate | 0.4426 |
| sharpe_ratio | -13.7722 |
| sortino_ratio | -7.4363 |
| max_drawdown | 0.9999 |
| cagr | -0.9782 |
| net_avg_win | 3.9405 |
| net_avg_loss | -14.2957 |
| avg_hold_time_bars | 2.2262 |
| exposure | 0.1420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
