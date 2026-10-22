# EMA Hourly Continuation — AXS/USDT P26_55

**Symbol:** AXS/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 852 |
| net_profit_factor | 0.5494 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 1.0384 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -6.0763 |
| sortino_ratio | -2.5029 |
| max_drawdown | 0.9562 |
| cagr | -0.7046 |
| net_avg_win | 28.7878 |
| net_avg_loss | -47.2518 |
| avg_hold_time_bars | 4.3040 |
| exposure | 0.1659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
