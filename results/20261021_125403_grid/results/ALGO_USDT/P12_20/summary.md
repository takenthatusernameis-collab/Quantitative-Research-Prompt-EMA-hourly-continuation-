# EMA Hourly Continuation — ALGO/USDT P12_20

**Symbol:** ALGO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.9252 |
| net_win_rate | 0.5714 |
| gross_profit_factor | 1.3196 |
| gross_win_rate | 0.5714 |
| sharpe_ratio | -0.3473 |
| sortino_ratio | -0.0805 |
| max_drawdown | 0.2438 |
| cagr | -0.0391 |
| net_avg_win | 81.8071 |
| net_avg_loss | -117.8928 |
| avg_hold_time_bars | 4.3889 |
| exposure | 0.0503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
