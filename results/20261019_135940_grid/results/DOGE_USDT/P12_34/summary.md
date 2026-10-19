# EMA Hourly Continuation — DOGE/USDT P12_34

**Symbol:** DOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1278 |
| net_profit_factor | 0.4244 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.8815 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -9.7446 |
| sortino_ratio | -4.8754 |
| max_drawdown | 0.9982 |
| cagr | -0.9186 |
| net_avg_win | 13.0043 |
| net_avg_loss | -24.3568 |
| avg_hold_time_bars | 3.6307 |
| exposure | 0.2109 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
