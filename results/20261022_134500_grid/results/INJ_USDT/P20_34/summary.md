# EMA Hourly Continuation — INJ/USDT P20_34

**Symbol:** INJ/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1181 |
| net_profit_factor | 0.4220 |
| net_win_rate | 0.4301 |
| gross_profit_factor | 0.8464 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -9.5250 |
| sortino_ratio | -4.6233 |
| max_drawdown | 0.9971 |
| cagr | -0.9017 |
| net_avg_win | 14.3284 |
| net_avg_loss | -25.6305 |
| avg_hold_time_bars | 2.3827 |
| exposure | 0.1279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
