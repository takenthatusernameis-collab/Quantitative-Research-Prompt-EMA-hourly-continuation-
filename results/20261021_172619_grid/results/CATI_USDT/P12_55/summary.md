# EMA Hourly Continuation — CATI/USDT P12_55

**Symbol:** CATI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.6387 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.7935 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -3.2865 |
| sortino_ratio | -1.1138 |
| max_drawdown | 0.6747 |
| cagr | -0.4030 |
| net_avg_win | 54.6436 |
| net_avg_loss | -69.5560 |
| avg_hold_time_bars | 14.3200 |
| exposure | 0.3729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
