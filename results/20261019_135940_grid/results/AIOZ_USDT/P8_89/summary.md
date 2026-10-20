# EMA Hourly Continuation — AIOZ/USDT P8_89

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 836 |
| net_profit_factor | 0.7104 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 1.0021 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -4.0353 |
| sortino_ratio | -1.6392 |
| max_drawdown | 0.8776 |
| cagr | -0.5446 |
| net_avg_win | 52.1656 |
| net_avg_loss | -69.0013 |
| avg_hold_time_bars | 16.4605 |
| exposure | 0.6255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
