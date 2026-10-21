# EMA Hourly Continuation — CHR/USDT P8_21

**Symbol:** CHR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.7355 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 1.0093 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -2.9157 |
| sortino_ratio | -1.1180 |
| max_drawdown | 0.7368 |
| cagr | -0.4001 |
| net_avg_win | 56.9163 |
| net_avg_loss | -75.2564 |
| avg_hold_time_bars | 5.9304 |
| exposure | 0.1927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
