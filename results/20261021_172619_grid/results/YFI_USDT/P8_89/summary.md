# EMA Hourly Continuation — YFI/USDT P8_89

**Symbol:** YFI/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.7409 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 0.9963 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -2.2983 |
| sortino_ratio | -0.7602 |
| max_drawdown | 0.6010 |
| cagr | -0.2956 |
| net_avg_win | 62.8452 |
| net_avg_loss | -83.8800 |
| avg_hold_time_bars | 26.7840 |
| exposure | 0.6508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
