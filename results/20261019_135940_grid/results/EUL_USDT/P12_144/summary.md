# EMA Hourly Continuation — EUL/USDT P12_144

**Symbol:** EUL/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.6040 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.8449 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -3.3124 |
| sortino_ratio | -1.1141 |
| max_drawdown | 0.7444 |
| cagr | -0.4070 |
| net_avg_win | 42.5439 |
| net_avg_loss | -60.5048 |
| avg_hold_time_bars | 23.9312 |
| exposure | 0.6168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
