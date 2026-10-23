# EMA Hourly Continuation — CTSI/USDT P34_144

**Symbol:** CTSI/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.5408 |
| net_win_rate | 0.4231 |
| gross_profit_factor | 0.7808 |
| gross_win_rate | 0.4327 |
| sharpe_ratio | -4.5580 |
| sortino_ratio | -1.4678 |
| max_drawdown | 0.8269 |
| cagr | -0.4995 |
| net_avg_win | 44.1126 |
| net_avg_loss | -59.8220 |
| avg_hold_time_bars | 18.8558 |
| exposure | 0.4457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
