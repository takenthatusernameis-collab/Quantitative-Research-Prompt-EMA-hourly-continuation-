# EMA Hourly Continuation — SATS/USDT P20_50

**Symbol:** SATS/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 901 |
| net_profit_factor | 0.5400 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.8898 |
| gross_win_rate | 0.4462 |
| sharpe_ratio | -6.2797 |
| sortino_ratio | -2.6472 |
| max_drawdown | 0.9609 |
| cagr | -0.7199 |
| net_avg_win | 28.3021 |
| net_avg_loss | -41.4729 |
| avg_hold_time_bars | 5.2386 |
| exposure | 0.2136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
