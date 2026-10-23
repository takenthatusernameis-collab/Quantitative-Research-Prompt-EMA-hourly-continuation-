# EMA Hourly Continuation — PUFFER/USDT P34_89

**Symbol:** PUFFER/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.7388 |
| net_win_rate | 0.5080 |
| gross_profit_factor | 1.0587 |
| gross_win_rate | 0.5159 |
| sharpe_ratio | -2.3332 |
| sortino_ratio | -0.8294 |
| max_drawdown | 0.5661 |
| cagr | -0.3221 |
| net_avg_win | 60.2951 |
| net_avg_loss | -84.2535 |
| avg_hold_time_bars | 8.6355 |
| exposure | 0.2453 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
