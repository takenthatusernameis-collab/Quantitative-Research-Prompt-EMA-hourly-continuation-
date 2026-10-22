# EMA Hourly Continuation — SUN/USDT P26_144

**Symbol:** SUN/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.3707 |
| net_win_rate | 0.3853 |
| gross_profit_factor | 0.7324 |
| gross_win_rate | 0.4209 |
| sharpe_ratio | -6.6683 |
| sortino_ratio | -1.9775 |
| max_drawdown | 0.9246 |
| cagr | -0.6406 |
| net_avg_win | 31.4781 |
| net_avg_loss | -53.2200 |
| avg_hold_time_bars | 23.6837 |
| exposure | 0.4812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
