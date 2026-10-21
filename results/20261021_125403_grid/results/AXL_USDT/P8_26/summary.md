# EMA Hourly Continuation — AXL/USDT P8_26

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 772 |
| net_profit_factor | 0.6466 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.8420 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -4.4298 |
| sortino_ratio | -1.7437 |
| max_drawdown | 0.8737 |
| cagr | -0.5529 |
| net_avg_win | 46.4754 |
| net_avg_loss | -57.1673 |
| avg_hold_time_bars | 6.7746 |
| exposure | 0.2367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
