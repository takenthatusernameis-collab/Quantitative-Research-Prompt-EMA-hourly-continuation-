# EMA Hourly Continuation — DOT/USDT P12_20

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.6351 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9128 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -2.2316 |
| sortino_ratio | -0.4998 |
| max_drawdown | 0.4549 |
| cagr | -0.2039 |
| net_avg_win | 65.4012 |
| net_avg_loss | -93.3264 |
| avg_hold_time_bars | 4.5656 |
| exposure | 0.0506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
