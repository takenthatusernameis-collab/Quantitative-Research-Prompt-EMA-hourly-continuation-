# EMA Hourly Continuation — MEME/USDT P21_34

**Symbol:** MEME/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.6121 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.8497 |
| gross_win_rate | 0.4581 |
| sharpe_ratio | -3.0027 |
| sortino_ratio | -0.8113 |
| max_drawdown | 0.6139 |
| cagr | -0.3104 |
| net_avg_win | 58.3779 |
| net_avg_loss | -80.6292 |
| avg_hold_time_bars | 4.8464 |
| exposure | 0.0789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
