# EMA Hourly Continuation — YFI/USDT P34_50

**Symbol:** YFI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1018 |
| net_profit_factor | 0.2840 |
| net_win_rate | 0.3792 |
| gross_profit_factor | 0.8553 |
| gross_win_rate | 0.4303 |
| sharpe_ratio | -12.3645 |
| sortino_ratio | -5.7041 |
| max_drawdown | 0.9994 |
| cagr | -0.9476 |
| net_avg_win | 10.2689 |
| net_avg_loss | -22.0853 |
| avg_hold_time_bars | 3.0442 |
| exposure | 0.1402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
