# EMA Hourly Continuation — CETUS/USDT P12_89

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.7037 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.9878 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -3.3805 |
| sortino_ratio | -1.2563 |
| max_drawdown | 0.7966 |
| cagr | -0.4550 |
| net_avg_win | 54.7388 |
| net_avg_loss | -72.8591 |
| avg_hold_time_bars | 17.7582 |
| exposure | 0.5649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
