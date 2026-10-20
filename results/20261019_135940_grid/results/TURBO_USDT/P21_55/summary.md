# EMA Hourly Continuation — TURBO/USDT P21_55

**Symbol:** TURBO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 807 |
| net_profit_factor | 0.6363 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9829 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -5.3368 |
| sortino_ratio | -2.3382 |
| max_drawdown | 0.9090 |
| cagr | -0.6753 |
| net_avg_win | 41.0191 |
| net_avg_loss | -59.1049 |
| avg_hold_time_bars | 5.2069 |
| exposure | 0.2292 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
