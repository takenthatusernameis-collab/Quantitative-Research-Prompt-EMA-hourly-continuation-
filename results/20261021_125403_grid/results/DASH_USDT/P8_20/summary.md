# EMA Hourly Continuation — DASH/USDT P8_20

**Symbol:** DASH/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.7516 |
| net_win_rate | 0.5170 |
| gross_profit_factor | 1.0679 |
| gross_win_rate | 0.5170 |
| sharpe_ratio | -1.8463 |
| sortino_ratio | -0.5766 |
| max_drawdown | 0.5323 |
| cagr | -0.2327 |
| net_avg_win | 60.4936 |
| net_avg_loss | -86.1615 |
| avg_hold_time_bars | 5.6085 |
| exposure | 0.1198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
