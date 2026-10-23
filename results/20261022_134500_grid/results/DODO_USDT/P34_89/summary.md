# EMA Hourly Continuation — DODO/USDT P34_89

**Symbol:** DODO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 782 |
| net_profit_factor | 0.5391 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.8595 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -6.3044 |
| sortino_ratio | -2.4642 |
| max_drawdown | 0.9542 |
| cagr | -0.7009 |
| net_avg_win | 32.7655 |
| net_avg_loss | -46.7517 |
| avg_hold_time_bars | 6.7327 |
| exposure | 0.2382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
