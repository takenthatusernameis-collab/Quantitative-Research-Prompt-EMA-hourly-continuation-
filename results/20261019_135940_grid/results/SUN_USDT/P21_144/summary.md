# EMA Hourly Continuation — SUN/USDT P21_144

**Symbol:** SUN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.3948 |
| net_win_rate | 0.3879 |
| gross_profit_factor | 0.7740 |
| gross_win_rate | 0.4305 |
| sharpe_ratio | -6.4385 |
| sortino_ratio | -1.9079 |
| max_drawdown | 0.9151 |
| cagr | -0.6224 |
| net_avg_win | 34.4779 |
| net_avg_loss | -55.3394 |
| avg_hold_time_bars | 28.5516 |
| exposure | 0.5763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
