# EMA Hourly Continuation — ARPA/USDT P20_144

**Symbol:** ARPA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.5934 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8598 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -4.2607 |
| sortino_ratio | -1.4612 |
| max_drawdown | 0.8320 |
| cagr | -0.4962 |
| net_avg_win | 45.2949 |
| net_avg_loss | -62.4366 |
| avg_hold_time_bars | 20.0221 |
| exposure | 0.5336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
