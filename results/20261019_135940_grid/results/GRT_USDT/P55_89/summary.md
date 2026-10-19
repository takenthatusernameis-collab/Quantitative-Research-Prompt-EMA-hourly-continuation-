# EMA Hourly Continuation — GRT/USDT P55_89

**Symbol:** GRT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.4797 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.8935 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -6.0374 |
| sortino_ratio | -2.2061 |
| max_drawdown | 0.9374 |
| cagr | -0.6613 |
| net_avg_win | 28.2645 |
| net_avg_loss | -48.9626 |
| avg_hold_time_bars | 3.7708 |
| exposure | 0.1147 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
