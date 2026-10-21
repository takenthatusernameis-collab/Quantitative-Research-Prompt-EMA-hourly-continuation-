# EMA Hourly Continuation — TIA/USDT P21_55

**Symbol:** TIA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.9202 |
| net_win_rate | 0.5344 |
| gross_profit_factor | 1.1406 |
| gross_win_rate | 0.5344 |
| sharpe_ratio | -0.5541 |
| sortino_ratio | -0.1780 |
| max_drawdown | 0.3451 |
| cagr | -0.0839 |
| net_avg_win | 86.2413 |
| net_avg_loss | -107.5770 |
| avg_hold_time_bars | 8.5020 |
| exposure | 0.1909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
