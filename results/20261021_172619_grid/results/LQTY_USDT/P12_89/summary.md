# EMA Hourly Continuation — LQTY/USDT P12_89

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.8252 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0254 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -1.2762 |
| sortino_ratio | -0.3987 |
| max_drawdown | 0.4083 |
| cagr | -0.1697 |
| net_avg_win | 72.7219 |
| net_avg_loss | -91.5208 |
| avg_hold_time_bars | 27.4361 |
| exposure | 0.5922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
