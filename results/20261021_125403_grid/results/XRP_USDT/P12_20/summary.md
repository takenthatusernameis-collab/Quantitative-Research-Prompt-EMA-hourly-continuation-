# EMA Hourly Continuation — XRP/USDT P12_20

**Symbol:** XRP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.7324 |
| net_win_rate | 0.5392 |
| gross_profit_factor | 1.1526 |
| gross_win_rate | 0.5392 |
| sharpe_ratio | -1.3363 |
| sortino_ratio | -0.2855 |
| max_drawdown | 0.2891 |
| cagr | -0.1214 |
| net_avg_win | 64.9421 |
| net_avg_loss | -103.7396 |
| avg_hold_time_bars | 5.2258 |
| exposure | 0.0515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
