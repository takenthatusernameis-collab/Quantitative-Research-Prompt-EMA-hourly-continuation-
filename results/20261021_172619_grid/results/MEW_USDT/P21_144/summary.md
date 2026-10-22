# EMA Hourly Continuation — MEW/USDT P21_144

**Symbol:** MEW/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.8483 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 1.0034 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -0.9955 |
| sortino_ratio | -0.2823 |
| max_drawdown | 0.3279 |
| cagr | -0.1238 |
| net_avg_win | 80.1379 |
| net_avg_loss | -95.4394 |
| avg_hold_time_bars | 28.0281 |
| exposure | 0.4994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
