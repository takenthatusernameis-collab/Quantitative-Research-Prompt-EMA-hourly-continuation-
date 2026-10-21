# EMA Hourly Continuation — AXL/USDT P20_144

**Symbol:** AXL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.7951 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9502 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -1.6304 |
| sortino_ratio | -0.4919 |
| max_drawdown | 0.4583 |
| cagr | -0.2044 |
| net_avg_win | 78.0238 |
| net_avg_loss | -92.2052 |
| avg_hold_time_bars | 25.4000 |
| exposure | 0.5172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
