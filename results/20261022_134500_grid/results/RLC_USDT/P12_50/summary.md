# EMA Hourly Continuation — RLC/USDT P12_50

**Symbol:** RLC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 950 |
| net_profit_factor | 0.5954 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.9621 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -5.6988 |
| sortino_ratio | -2.4458 |
| max_drawdown | 0.9551 |
| cagr | -0.7020 |
| net_avg_win | 31.2101 |
| net_avg_loss | -46.9763 |
| avg_hold_time_bars | 8.8263 |
| exposure | 0.3811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
