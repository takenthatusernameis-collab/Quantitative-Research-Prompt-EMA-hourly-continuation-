# EMA Hourly Continuation — PEOPLE/USDT P34_200

**Symbol:** PEOPLE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7341 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 1.0064 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -1.8170 |
| sortino_ratio | -0.5013 |
| max_drawdown | 0.5074 |
| cagr | -0.2150 |
| net_avg_win | 65.3502 |
| net_avg_loss | -88.5668 |
| avg_hold_time_bars | 28.7674 |
| exposure | 0.5038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
