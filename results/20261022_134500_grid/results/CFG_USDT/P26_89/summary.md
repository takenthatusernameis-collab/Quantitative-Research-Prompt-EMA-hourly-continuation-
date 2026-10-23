# EMA Hourly Continuation — CFG/USDT P26_89

**Symbol:** CFG/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.5545 |
| net_win_rate | 0.4311 |
| gross_profit_factor | 0.8109 |
| gross_win_rate | 0.4346 |
| sharpe_ratio | -4.5460 |
| sortino_ratio | -1.5328 |
| max_drawdown | 0.8480 |
| cagr | -0.5164 |
| net_avg_win | 42.2549 |
| net_avg_loss | -57.7416 |
| avg_hold_time_bars | 17.7068 |
| exposure | 0.4612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
