# EMA Hourly Continuation — G/USDT P26_34

**Symbol:** G/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 837 |
| net_profit_factor | 0.3460 |
| net_win_rate | 0.3978 |
| gross_profit_factor | 0.9420 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -10.4674 |
| sortino_ratio | -4.6897 |
| max_drawdown | 0.9938 |
| cagr | -0.9033 |
| net_avg_win | 15.7911 |
| net_avg_loss | -30.1502 |
| avg_hold_time_bars | 3.4038 |
| exposure | 0.1498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
