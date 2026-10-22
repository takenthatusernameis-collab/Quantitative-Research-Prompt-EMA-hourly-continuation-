# EMA Hourly Continuation — PIXEL/USDT P12_89

**Symbol:** PIXEL/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.7239 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9910 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -3.0415 |
| sortino_ratio | -1.1339 |
| max_drawdown | 0.7434 |
| cagr | -0.4138 |
| net_avg_win | 57.5797 |
| net_avg_loss | -74.2526 |
| avg_hold_time_bars | 18.6547 |
| exposure | 0.5892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
