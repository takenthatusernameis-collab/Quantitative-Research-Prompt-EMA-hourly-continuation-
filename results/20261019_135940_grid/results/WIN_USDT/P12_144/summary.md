# EMA Hourly Continuation — WIN/USDT P12_144

**Symbol:** WIN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.5253 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.8756 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -3.8433 |
| sortino_ratio | -1.1743 |
| max_drawdown | 0.7818 |
| cagr | -0.4391 |
| net_avg_win | 37.6725 |
| net_avg_loss | -64.2826 |
| avg_hold_time_bars | 31.5105 |
| exposure | 0.6818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
