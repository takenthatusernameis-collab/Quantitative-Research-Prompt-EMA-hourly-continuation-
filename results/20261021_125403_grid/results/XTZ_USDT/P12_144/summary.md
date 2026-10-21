# EMA Hourly Continuation — XTZ/USDT P12_144

**Symbol:** XTZ/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.9171 |
| net_win_rate | 0.5350 |
| gross_profit_factor | 1.1421 |
| gross_win_rate | 0.5350 |
| sharpe_ratio | -0.4190 |
| sortino_ratio | -0.1098 |
| max_drawdown | 0.1915 |
| cagr | -0.0531 |
| net_avg_win | 80.5583 |
| net_avg_loss | -101.0435 |
| avg_hold_time_bars | 47.9514 |
| exposure | 0.7171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
