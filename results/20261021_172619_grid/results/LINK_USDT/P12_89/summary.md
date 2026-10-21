# EMA Hourly Continuation — LINK/USDT P12_89

**Symbol:** LINK/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.7963 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 1.0017 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -1.8496 |
| sortino_ratio | -0.5860 |
| max_drawdown | 0.5463 |
| cagr | -0.2373 |
| net_avg_win | 79.7328 |
| net_avg_loss | -97.3128 |
| avg_hold_time_bars | 22.0631 |
| exposure | 0.4924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
