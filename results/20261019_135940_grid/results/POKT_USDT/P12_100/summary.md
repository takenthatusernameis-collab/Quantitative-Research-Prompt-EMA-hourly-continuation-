# EMA Hourly Continuation — POKT/USDT P12_100

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 817 |
| net_profit_factor | 0.5717 |
| net_win_rate | 0.4064 |
| gross_profit_factor | 0.8486 |
| gross_win_rate | 0.4125 |
| sharpe_ratio | -6.5217 |
| sortino_ratio | -2.6008 |
| max_drawdown | 0.9594 |
| cagr | -0.7159 |
| net_avg_win | 38.5318 |
| net_avg_loss | -46.1330 |
| avg_hold_time_bars | 15.5092 |
| exposure | 0.5734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
