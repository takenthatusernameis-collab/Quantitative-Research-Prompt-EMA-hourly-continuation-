# EMA Hourly Continuation — FLR/USDT P55_89

**Symbol:** FLR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.6132 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.8823 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -2.6637 |
| sortino_ratio | -0.6753 |
| max_drawdown | 0.5441 |
| cagr | -0.2660 |
| net_avg_win | 57.8512 |
| net_avg_loss | -84.6199 |
| avg_hold_time_bars | 6.0128 |
| exposure | 0.0855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
