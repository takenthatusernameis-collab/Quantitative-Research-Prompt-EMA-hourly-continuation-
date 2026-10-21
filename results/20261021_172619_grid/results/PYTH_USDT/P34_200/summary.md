# EMA Hourly Continuation — PYTH/USDT P34_200

**Symbol:** PYTH/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.9367 |
| net_win_rate | 0.5211 |
| gross_profit_factor | 1.0796 |
| gross_win_rate | 0.5211 |
| sharpe_ratio | -0.2936 |
| sortino_ratio | -0.0683 |
| max_drawdown | 0.1729 |
| cagr | -0.0345 |
| net_avg_win | 91.8039 |
| net_avg_loss | -106.6312 |
| avg_hold_time_bars | 43.7356 |
| exposure | 0.5189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
