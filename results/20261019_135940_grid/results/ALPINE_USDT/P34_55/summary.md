# EMA Hourly Continuation — ALPINE/USDT P34_55

**Symbol:** ALPINE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 822 |
| net_profit_factor | 0.3755 |
| net_win_rate | 0.4039 |
| gross_profit_factor | 0.7649 |
| gross_win_rate | 0.4343 |
| sharpe_ratio | -8.8445 |
| sortino_ratio | -3.6122 |
| max_drawdown | 0.9889 |
| cagr | -0.8325 |
| net_avg_win | 17.9047 |
| net_avg_loss | -32.3099 |
| avg_hold_time_bars | 4.6484 |
| exposure | 0.1737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
