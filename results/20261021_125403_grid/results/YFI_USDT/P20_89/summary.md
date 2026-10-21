# EMA Hourly Continuation — YFI/USDT P20_89

**Symbol:** YFI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.7225 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 1.0139 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -2.7041 |
| sortino_ratio | -0.9196 |
| max_drawdown | 0.6882 |
| cagr | -0.3436 |
| net_avg_win | 60.8381 |
| net_avg_loss | -82.4375 |
| avg_hold_time_bars | 14.6837 |
| exposure | 0.3761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
