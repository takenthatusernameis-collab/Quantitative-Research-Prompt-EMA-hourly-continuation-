# EMA Hourly Continuation — PEPE/USDT P20_89

**Symbol:** PEPE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.7262 |
| net_win_rate | 0.4703 |
| gross_profit_factor | 0.8809 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -2.0492 |
| sortino_ratio | -0.5981 |
| max_drawdown | 0.5176 |
| cagr | -0.2404 |
| net_avg_win | 66.7875 |
| net_avg_loss | -81.6635 |
| avg_hold_time_bars | 19.8765 |
| exposure | 0.3804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
