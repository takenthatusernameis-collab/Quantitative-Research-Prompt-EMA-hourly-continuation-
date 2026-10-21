# EMA Hourly Continuation — CGPT/USDT P144_200

**Symbol:** CGPT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 199 |
| net_profit_factor | 0.7845 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0467 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -1.0584 |
| sortino_ratio | -0.2148 |
| max_drawdown | 0.2631 |
| cagr | -0.0941 |
| net_avg_win | 78.4233 |
| net_avg_loss | -105.1223 |
| avg_hold_time_bars | 7.1859 |
| exposure | 0.0650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
