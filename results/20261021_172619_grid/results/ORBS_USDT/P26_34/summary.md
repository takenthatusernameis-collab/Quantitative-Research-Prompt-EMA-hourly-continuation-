# EMA Hourly Continuation — ORBS/USDT P26_34

**Symbol:** ORBS/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.4533 |
| net_win_rate | 0.4012 |
| gross_profit_factor | 0.7699 |
| gross_win_rate | 0.4041 |
| sharpe_ratio | -5.0725 |
| sortino_ratio | -1.3430 |
| max_drawdown | 0.7980 |
| cagr | -0.4638 |
| net_avg_win | 48.2288 |
| net_avg_loss | -71.2715 |
| avg_hold_time_bars | 6.2419 |
| exposure | 0.0962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
