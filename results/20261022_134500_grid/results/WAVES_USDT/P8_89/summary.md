# EMA Hourly Continuation — WAVES/USDT P8_89

**Symbol:** WAVES/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 950 |
| net_profit_factor | 0.5234 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.8826 |
| gross_win_rate | 0.4632 |
| sharpe_ratio | -7.0838 |
| sortino_ratio | -3.0339 |
| max_drawdown | 0.9796 |
| cagr | -0.7854 |
| net_avg_win | 25.6587 |
| net_avg_loss | -38.6842 |
| avg_hold_time_bars | 13.7263 |
| exposure | 0.5927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
