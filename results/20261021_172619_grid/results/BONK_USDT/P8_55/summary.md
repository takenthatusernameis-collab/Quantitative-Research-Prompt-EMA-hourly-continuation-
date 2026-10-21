# EMA Hourly Continuation — BONK/USDT P8_55

**Symbol:** BONK/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.8875 |
| net_win_rate | 0.5145 |
| gross_profit_factor | 1.0537 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -0.9607 |
| sortino_ratio | -0.3539 |
| max_drawdown | 0.5199 |
| cagr | -0.1554 |
| net_avg_win | 80.6810 |
| net_avg_loss | -96.3226 |
| avg_hold_time_bars | 14.3744 |
| exposure | 0.4293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
