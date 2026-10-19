# EMA Hourly Continuation — CHZ/USDT P26_89

**Symbol:** CHZ/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.5685 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9192 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -4.5467 |
| sortino_ratio | -1.6437 |
| max_drawdown | 0.8699 |
| cagr | -0.5518 |
| net_avg_win | 36.1426 |
| net_avg_loss | -57.8917 |
| avg_hold_time_bars | 10.6244 |
| exposure | 0.3202 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
