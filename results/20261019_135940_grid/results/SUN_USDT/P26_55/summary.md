# EMA Hourly Continuation — SUN/USDT P26_55

**Symbol:** SUN/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 797 |
| net_profit_factor | 0.2360 |
| net_win_rate | 0.3375 |
| gross_profit_factor | 0.7290 |
| gross_win_rate | 0.4053 |
| sharpe_ratio | -12.0914 |
| sortino_ratio | -4.9751 |
| max_drawdown | 0.9988 |
| cagr | -0.9301 |
| net_avg_win | 11.4669 |
| net_avg_loss | -24.7584 |
| avg_hold_time_bars | 5.9335 |
| exposure | 0.2140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
