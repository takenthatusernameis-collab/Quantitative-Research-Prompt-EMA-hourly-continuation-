# EMA Hourly Continuation — MOCA/USDT P55_89

**Symbol:** MOCA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.6571 |
| net_win_rate | 0.4768 |
| gross_profit_factor | 0.8958 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -2.3696 |
| sortino_ratio | -0.6182 |
| max_drawdown | 0.4880 |
| cagr | -0.2468 |
| net_avg_win | 63.2820 |
| net_avg_loss | -87.7701 |
| avg_hold_time_bars | 6.6258 |
| exposure | 0.1003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
