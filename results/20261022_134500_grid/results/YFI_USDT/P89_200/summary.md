# EMA Hourly Continuation — YFI/USDT P89_200

**Symbol:** YFI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.5039 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9598 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -3.7558 |
| sortino_ratio | -1.0843 |
| max_drawdown | 0.7502 |
| cagr | -0.4059 |
| net_avg_win | 36.7649 |
| net_avg_loss | -67.6052 |
| avg_hold_time_bars | 12.1595 |
| exposure | 0.2311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
