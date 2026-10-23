# EMA Hourly Continuation — NYM/USDT P55_89

**Symbol:** NYM/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.1770 |
| net_win_rate | 0.3054 |
| gross_profit_factor | 0.4967 |
| gross_win_rate | 0.3393 |
| sharpe_ratio | -10.7454 |
| sortino_ratio | -3.7391 |
| max_drawdown | 0.9935 |
| cagr | -0.8653 |
| net_avg_win | 12.4933 |
| net_avg_loss | -31.0316 |
| avg_hold_time_bars | 5.4071 |
| exposure | 0.1376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
