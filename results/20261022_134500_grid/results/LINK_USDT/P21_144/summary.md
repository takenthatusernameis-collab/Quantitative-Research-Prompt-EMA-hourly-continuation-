# EMA Hourly Continuation — LINK/USDT P21_144

**Symbol:** LINK/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6988 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0596 |
| gross_win_rate | 0.5191 |
| sharpe_ratio | -2.4583 |
| sortino_ratio | -0.7515 |
| max_drawdown | 0.6162 |
| cagr | -0.3007 |
| net_avg_win | 57.0514 |
| net_avg_loss | -85.1781 |
| avg_hold_time_bars | 24.0233 |
| exposure | 0.5154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
