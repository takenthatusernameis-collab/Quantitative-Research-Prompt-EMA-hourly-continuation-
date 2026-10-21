# EMA Hourly Continuation — MASK/USDT P20_89

**Symbol:** MASK/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.5721 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.7890 |
| gross_win_rate | 0.4461 |
| sharpe_ratio | -3.9473 |
| sortino_ratio | -1.2989 |
| max_drawdown | 0.7917 |
| cagr | -0.4524 |
| net_avg_win | 43.8002 |
| net_avg_loss | -60.7356 |
| avg_hold_time_bars | 16.5130 |
| exposure | 0.4038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
