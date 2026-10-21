# EMA Hourly Continuation — ARPA/USDT P20_55

**Symbol:** ARPA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.6467 |
| net_win_rate | 0.4594 |
| gross_profit_factor | 0.9033 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -4.0637 |
| sortino_ratio | -1.4642 |
| max_drawdown | 0.8234 |
| cagr | -0.4888 |
| net_avg_win | 50.7922 |
| net_avg_loss | -66.7412 |
| avg_hold_time_bars | 8.1922 |
| exposure | 0.2373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
