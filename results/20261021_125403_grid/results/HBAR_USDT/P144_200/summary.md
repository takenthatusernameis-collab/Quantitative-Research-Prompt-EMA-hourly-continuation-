# EMA Hourly Continuation — HBAR/USDT P144_200

**Symbol:** HBAR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 165 |
| net_profit_factor | 0.7592 |
| net_win_rate | 0.5152 |
| gross_profit_factor | 1.0592 |
| gross_win_rate | 0.5152 |
| sharpe_ratio | -1.1050 |
| sortino_ratio | -0.2044 |
| max_drawdown | 0.2471 |
| cagr | -0.0896 |
| net_avg_win | 77.9240 |
| net_avg_loss | -109.0489 |
| avg_hold_time_bars | 8.1636 |
| exposure | 0.0612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
