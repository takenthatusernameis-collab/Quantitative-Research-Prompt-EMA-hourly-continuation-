# EMA Hourly Continuation — CHZ/USDT P12_89

**Symbol:** CHZ/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.9069 |
| net_win_rate | 0.5298 |
| gross_profit_factor | 1.1165 |
| gross_win_rate | 0.5298 |
| sharpe_ratio | -0.6027 |
| sortino_ratio | -0.1952 |
| max_drawdown | 0.3290 |
| cagr | -0.0912 |
| net_avg_win | 77.9243 |
| net_avg_loss | -96.7963 |
| avg_hold_time_bars | 22.7341 |
| exposure | 0.5208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
