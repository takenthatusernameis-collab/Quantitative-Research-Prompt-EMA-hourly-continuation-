# EMA Hourly Continuation — WIN/USDT P12_55

**Symbol:** WIN/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.6346 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.9113 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -3.5753 |
| sortino_ratio | -1.2653 |
| max_drawdown | 0.7895 |
| cagr | -0.4408 |
| net_avg_win | 45.9774 |
| net_avg_loss | -65.2496 |
| avg_hold_time_bars | 12.0801 |
| exposure | 0.3360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
