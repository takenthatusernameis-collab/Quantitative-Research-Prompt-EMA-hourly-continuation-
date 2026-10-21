# EMA Hourly Continuation — TURBO/USDT P20_89

**Symbol:** TURBO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.7843 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9474 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -1.7902 |
| sortino_ratio | -0.5758 |
| max_drawdown | 0.5153 |
| cagr | -0.2336 |
| net_avg_win | 75.0001 |
| net_avg_loss | -91.2161 |
| avg_hold_time_bars | 15.2217 |
| exposure | 0.3521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
