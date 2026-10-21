# EMA Hourly Continuation — BDX/USDT P100_200

**Symbol:** BDX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.5413 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.8785 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -2.8198 |
| sortino_ratio | -0.6873 |
| max_drawdown | 0.5688 |
| cagr | -0.2692 |
| net_avg_win | 46.2827 |
| net_avg_loss | -80.2995 |
| avg_hold_time_bars | 10.3206 |
| exposure | 0.1346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
