# EMA Hourly Continuation — EWT/USDT P26_55

**Symbol:** EWT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.6363 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.8433 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -2.7040 |
| sortino_ratio | -0.7386 |
| max_drawdown | 0.5781 |
| cagr | -0.2883 |
| net_avg_win | 59.4506 |
| net_avg_loss | -79.3496 |
| avg_hold_time_bars | 8.1332 |
| exposure | 0.1360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
