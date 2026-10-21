# EMA Hourly Continuation — PROM/USDT P12_55

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6495 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.8836 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -3.8952 |
| sortino_ratio | -1.4176 |
| max_drawdown | 0.8090 |
| cagr | -0.4819 |
| net_avg_win | 50.0835 |
| net_avg_loss | -64.4066 |
| avg_hold_time_bars | 12.5662 |
| exposure | 0.3753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
