# EMA Hourly Continuation — TRADE/USDT P34_89

**Symbol:** TRADE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 563 |
| net_profit_factor | 0.5016 |
| net_win_rate | 0.4316 |
| gross_profit_factor | 0.8021 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -5.1070 |
| sortino_ratio | -1.6928 |
| max_drawdown | 0.8837 |
| cagr | -0.5698 |
| net_avg_win | 36.4387 |
| net_avg_loss | -55.1633 |
| avg_hold_time_bars | 8.8952 |
| exposure | 0.2276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
