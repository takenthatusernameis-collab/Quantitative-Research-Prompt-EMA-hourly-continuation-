# EMA Hourly Continuation — DOT/USDT P20_34

**Symbol:** DOT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.6507 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9524 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -2.2816 |
| sortino_ratio | -0.5599 |
| max_drawdown | 0.4996 |
| cagr | -0.2245 |
| net_avg_win | 61.9134 |
| net_avg_loss | -90.0704 |
| avg_hold_time_bars | 5.3836 |
| exposure | 0.0715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
