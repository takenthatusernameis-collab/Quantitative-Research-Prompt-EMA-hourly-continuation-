# EMA Hourly Continuation — G/USDT P8_144

**Symbol:** G/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7296 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0834 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -1.9085 |
| sortino_ratio | -0.5443 |
| max_drawdown | 0.5373 |
| cagr | -0.2247 |
| net_avg_win | 65.0733 |
| net_avg_loss | -91.2681 |
| avg_hold_time_bars | 42.8506 |
| exposure | 0.7841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
