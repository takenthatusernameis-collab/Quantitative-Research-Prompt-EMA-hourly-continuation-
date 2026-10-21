# EMA Hourly Continuation — CHZ/USDT P26_144

**Symbol:** CHZ/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.9727 |
| net_win_rate | 0.5444 |
| gross_profit_factor | 1.1908 |
| gross_win_rate | 0.5444 |
| sharpe_ratio | -0.1056 |
| sortino_ratio | -0.0281 |
| max_drawdown | 0.2831 |
| cagr | -0.0188 |
| net_avg_win | 90.1652 |
| net_avg_loss | -110.7577 |
| avg_hold_time_bars | 32.7485 |
| exposure | 0.5031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
