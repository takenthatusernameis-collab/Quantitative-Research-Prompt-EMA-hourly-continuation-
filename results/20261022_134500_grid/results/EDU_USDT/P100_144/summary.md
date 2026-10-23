# EMA Hourly Continuation — EDU/USDT P100_144

**Symbol:** EDU/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.4885 |
| net_win_rate | 0.4312 |
| gross_profit_factor | 0.8340 |
| gross_win_rate | 0.4424 |
| sharpe_ratio | -5.5563 |
| sortino_ratio | -1.8120 |
| max_drawdown | 0.8990 |
| cagr | -0.5879 |
| net_avg_win | 36.7735 |
| net_avg_loss | -57.0690 |
| avg_hold_time_bars | 4.5112 |
| exposure | 0.1098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
