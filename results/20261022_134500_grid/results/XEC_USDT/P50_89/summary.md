# EMA Hourly Continuation — XEC/USDT P50_89

**Symbol:** XEC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.3517 |
| net_win_rate | 0.4140 |
| gross_profit_factor | 0.6826 |
| gross_win_rate | 0.4347 |
| sharpe_ratio | -7.5415 |
| sortino_ratio | -2.8733 |
| max_drawdown | 0.9729 |
| cagr | -0.7579 |
| net_avg_win | 17.5224 |
| net_avg_loss | -35.1996 |
| avg_hold_time_bars | 5.2201 |
| exposure | 0.1717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
