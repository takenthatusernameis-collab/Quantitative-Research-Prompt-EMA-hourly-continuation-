# EMA Hourly Continuation — ETC/USDT P20_100

**Symbol:** ETC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.7144 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 0.9824 |
| gross_win_rate | 0.4928 |
| sharpe_ratio | -2.3815 |
| sortino_ratio | -0.7491 |
| max_drawdown | 0.5914 |
| cagr | -0.2904 |
| net_avg_win | 60.6920 |
| net_avg_loss | -82.5282 |
| avg_hold_time_bars | 16.8137 |
| exposure | 0.3691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
