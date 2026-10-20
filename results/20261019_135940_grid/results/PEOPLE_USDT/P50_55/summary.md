# EMA Hourly Continuation — PEOPLE/USDT P50_55

**Symbol:** PEOPLE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 873 |
| net_profit_factor | 0.2932 |
| net_win_rate | 0.3711 |
| gross_profit_factor | 0.6304 |
| gross_win_rate | 0.4066 |
| sharpe_ratio | -11.4620 |
| sortino_ratio | -4.8686 |
| max_drawdown | 0.9985 |
| cagr | -0.9249 |
| net_avg_win | 12.7875 |
| net_avg_loss | -25.7351 |
| avg_hold_time_bars | 2.0115 |
| exposure | 0.0795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
