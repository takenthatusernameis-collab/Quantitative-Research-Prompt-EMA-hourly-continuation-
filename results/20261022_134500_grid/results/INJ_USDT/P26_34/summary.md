# EMA Hourly Continuation — INJ/USDT P26_34

**Symbol:** INJ/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1100 |
| net_profit_factor | 0.3028 |
| net_win_rate | 0.3927 |
| gross_profit_factor | 0.7167 |
| gross_win_rate | 0.4182 |
| sharpe_ratio | -11.7540 |
| sortino_ratio | -5.5995 |
| max_drawdown | 0.9993 |
| cagr | -0.9440 |
| net_avg_win | 10.0468 |
| net_avg_loss | -21.4567 |
| avg_hold_time_bars | 1.8382 |
| exposure | 0.0919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
