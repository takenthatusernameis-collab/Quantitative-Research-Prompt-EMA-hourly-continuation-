# EMA Hourly Continuation — ENS/USDT P12_55

**Symbol:** ENS/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1003 |
| net_profit_factor | 0.5444 |
| net_win_rate | 0.4546 |
| gross_profit_factor | 0.8484 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -6.5270 |
| sortino_ratio | -2.8939 |
| max_drawdown | 0.9718 |
| cagr | -0.7572 |
| net_avg_win | 25.4533 |
| net_avg_loss | -38.9780 |
| avg_hold_time_bars | 9.0100 |
| exposure | 0.4108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
