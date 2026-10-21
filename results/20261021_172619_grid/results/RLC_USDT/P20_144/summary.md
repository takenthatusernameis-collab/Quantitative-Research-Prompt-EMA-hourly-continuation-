# EMA Hourly Continuation — RLC/USDT P20_144

**Symbol:** RLC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.7803 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9653 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -1.5790 |
| sortino_ratio | -0.4757 |
| max_drawdown | 0.4678 |
| cagr | -0.1976 |
| net_avg_win | 68.2419 |
| net_avg_loss | -86.2842 |
| avg_hold_time_bars | 25.1303 |
| exposure | 0.5083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
