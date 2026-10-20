# EMA Hourly Continuation — AMP/USDT P20_21

**Symbol:** AMP/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1636 |
| net_profit_factor | 0.1056 |
| net_win_rate | 0.2384 |
| gross_profit_factor | 0.5037 |
| gross_win_rate | 0.3246 |
| sharpe_ratio | -23.3740 |
| sortino_ratio | -14.6490 |
| max_drawdown | 1.0000 |
| cagr | -0.9997 |
| net_avg_win | 3.0283 |
| net_avg_loss | -8.9736 |
| avg_hold_time_bars | 1.8050 |
| exposure | 0.1342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
