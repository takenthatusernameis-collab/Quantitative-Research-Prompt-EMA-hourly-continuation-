# EMA Hourly Continuation — MANA/USDT P34_55

**Symbol:** MANA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6855 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9867 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -2.2004 |
| sortino_ratio | -0.5797 |
| max_drawdown | 0.5242 |
| cagr | -0.2320 |
| net_avg_win | 63.6380 |
| net_avg_loss | -90.6517 |
| avg_hold_time_bars | 5.5565 |
| exposure | 0.0849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
