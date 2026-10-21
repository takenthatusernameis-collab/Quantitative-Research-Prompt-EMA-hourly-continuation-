# EMA Hourly Continuation — HTX/USDT P12_89

**Symbol:** HTX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.5364 |
| net_win_rate | 0.4367 |
| gross_profit_factor | 0.8636 |
| gross_win_rate | 0.4385 |
| sharpe_ratio | -5.6933 |
| sortino_ratio | -1.8993 |
| max_drawdown | 0.8986 |
| cagr | -0.5952 |
| net_avg_win | 43.6474 |
| net_avg_loss | -63.0839 |
| avg_hold_time_bars | 21.2606 |
| exposure | 0.5243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
