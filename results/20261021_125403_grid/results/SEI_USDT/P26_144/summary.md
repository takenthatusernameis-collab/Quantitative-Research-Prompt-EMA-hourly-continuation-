# EMA Hourly Continuation — SEI/USDT P26_144

**Symbol:** SEI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.9280 |
| net_win_rate | 0.5279 |
| gross_profit_factor | 1.1039 |
| gross_win_rate | 0.5279 |
| sharpe_ratio | -0.3849 |
| sortino_ratio | -0.1024 |
| max_drawdown | 0.2164 |
| cagr | -0.0504 |
| net_avg_win | 87.1933 |
| net_avg_loss | -105.0441 |
| avg_hold_time_bars | 33.1056 |
| exposure | 0.5131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
