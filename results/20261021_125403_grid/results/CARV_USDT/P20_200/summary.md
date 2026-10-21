# EMA Hourly Continuation — CARV/USDT P20_200

**Symbol:** CARV/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.6474 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.7792 |
| gross_win_rate | 0.4382 |
| sharpe_ratio | -2.5162 |
| sortino_ratio | -0.6655 |
| max_drawdown | 0.5037 |
| cagr | -0.2642 |
| net_avg_win | 68.6144 |
| net_avg_loss | -82.6527 |
| avg_hold_time_bars | 36.4594 |
| exposure | 0.5806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
