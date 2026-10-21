# EMA Hourly Continuation — CRV/USDT P8_26

**Symbol:** CRV/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.7786 |
| net_win_rate | 0.5153 |
| gross_profit_factor | 1.0239 |
| gross_win_rate | 0.5153 |
| sharpe_ratio | -1.6636 |
| sortino_ratio | -0.5964 |
| max_drawdown | 0.5300 |
| cagr | -0.2407 |
| net_avg_win | 54.8653 |
| net_avg_loss | -74.9149 |
| avg_hold_time_bars | 6.6345 |
| exposure | 0.1873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
