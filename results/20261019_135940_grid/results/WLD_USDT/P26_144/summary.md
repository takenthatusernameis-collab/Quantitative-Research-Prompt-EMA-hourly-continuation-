# EMA Hourly Continuation — WLD/USDT P26_144

**Symbol:** WLD/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.8375 |
| net_win_rate | 0.5268 |
| gross_profit_factor | 1.1249 |
| gross_win_rate | 0.5315 |
| sharpe_ratio | -1.0523 |
| sortino_ratio | -0.3097 |
| max_drawdown | 0.3601 |
| cagr | -0.1390 |
| net_avg_win | 71.4406 |
| net_avg_loss | -94.9720 |
| avg_hold_time_bars | 24.0023 |
| exposure | 0.4680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
