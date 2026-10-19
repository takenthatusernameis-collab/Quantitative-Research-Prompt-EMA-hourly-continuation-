# EMA Hourly Continuation — TRAC/USDT P20_100

**Symbol:** TRAC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.6773 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 1.0085 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -3.5082 |
| sortino_ratio | -1.2958 |
| max_drawdown | 0.8019 |
| cagr | -0.4651 |
| net_avg_win | 49.3443 |
| net_avg_loss | -68.7704 |
| avg_hold_time_bars | 11.6830 |
| exposure | 0.3685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
