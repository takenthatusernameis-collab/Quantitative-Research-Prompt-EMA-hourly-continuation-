# EMA Hourly Continuation — FIL/USDT P55_100

**Symbol:** FIL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.5797 |
| net_win_rate | 0.4403 |
| gross_profit_factor | 0.7763 |
| gross_win_rate | 0.4403 |
| sharpe_ratio | -2.8244 |
| sortino_ratio | -0.6877 |
| max_drawdown | 0.5485 |
| cagr | -0.2714 |
| net_avg_win | 58.6301 |
| net_avg_loss | -79.5605 |
| avg_hold_time_bars | 7.9488 |
| exposure | 0.1059 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
