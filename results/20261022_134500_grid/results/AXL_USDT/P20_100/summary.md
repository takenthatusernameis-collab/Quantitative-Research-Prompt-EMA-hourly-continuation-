# EMA Hourly Continuation — AXL/USDT P20_100

**Symbol:** AXL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 780 |
| net_profit_factor | 0.5874 |
| net_win_rate | 0.4308 |
| gross_profit_factor | 0.8444 |
| gross_win_rate | 0.4359 |
| sharpe_ratio | -5.5039 |
| sortino_ratio | -2.1538 |
| max_drawdown | 0.9274 |
| cagr | -0.6431 |
| net_avg_win | 39.2132 |
| net_avg_loss | -50.5231 |
| avg_hold_time_bars | 11.5974 |
| exposure | 0.4093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
