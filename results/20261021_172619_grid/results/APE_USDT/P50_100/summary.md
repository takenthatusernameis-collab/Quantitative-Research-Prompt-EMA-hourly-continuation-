# EMA Hourly Continuation — APE/USDT P50_100

**Symbol:** APE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.6824 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.8875 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -2.2906 |
| sortino_ratio | -0.6260 |
| max_drawdown | 0.5265 |
| cagr | -0.2496 |
| net_avg_win | 63.8059 |
| net_avg_loss | -83.3819 |
| avg_hold_time_bars | 9.8556 |
| exposure | 0.1644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
