# EMA Hourly Continuation — SUN/USDT P55_89

**Symbol:** SUN/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.2306 |
| net_win_rate | 0.3328 |
| gross_profit_factor | 0.6493 |
| gross_win_rate | 0.4062 |
| sharpe_ratio | -10.7457 |
| sortino_ratio | -3.8760 |
| max_drawdown | 0.9951 |
| cagr | -0.8782 |
| net_avg_win | 14.6185 |
| net_avg_loss | -31.6204 |
| avg_hold_time_bars | 5.3132 |
| exposure | 0.1474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
