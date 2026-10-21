# EMA Hourly Continuation — ETHFI/USDT P12_34

**Symbol:** ETHFI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.7133 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.8860 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -2.6665 |
| sortino_ratio | -0.8937 |
| max_drawdown | 0.6489 |
| cagr | -0.3371 |
| net_avg_win | 62.0846 |
| net_avg_loss | -75.6128 |
| avg_hold_time_bars | 7.7027 |
| exposure | 0.1943 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
