# EMA Hourly Continuation — W/USDT P55_89

**Symbol:** W/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.7347 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9563 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.5145 |
| sortino_ratio | -0.3788 |
| max_drawdown | 0.3768 |
| cagr | -0.1596 |
| net_avg_win | 64.4677 |
| net_avg_loss | -87.1758 |
| avg_hold_time_bars | 6.7738 |
| exposure | 0.0939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
