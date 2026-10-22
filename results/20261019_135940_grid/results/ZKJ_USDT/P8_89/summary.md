# EMA Hourly Continuation — ZKJ/USDT P8_89

**Symbol:** ZKJ/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.1853 |
| net_win_rate | 0.3165 |
| gross_profit_factor | 0.5049 |
| gross_win_rate | 0.3754 |
| sharpe_ratio | -8.5639 |
| sortino_ratio | -2.3798 |
| max_drawdown | 0.9632 |
| cagr | -0.7278 |
| net_avg_win | 19.3674 |
| net_avg_loss | -48.3923 |
| avg_hold_time_bars | 52.3782 |
| exposure | 0.8500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
