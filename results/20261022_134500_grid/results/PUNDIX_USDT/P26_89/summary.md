# EMA Hourly Continuation — PUNDIX/USDT P26_89

**Symbol:** PUNDIX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.5283 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.8584 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -5.1024 |
| sortino_ratio | -1.9004 |
| max_drawdown | 0.9020 |
| cagr | -0.5982 |
| net_avg_win | 31.6467 |
| net_avg_loss | -50.1329 |
| avg_hold_time_bars | 11.1476 |
| exposure | 0.3537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
