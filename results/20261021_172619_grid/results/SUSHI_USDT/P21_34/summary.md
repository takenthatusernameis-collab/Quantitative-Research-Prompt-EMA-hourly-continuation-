# EMA Hourly Continuation — SUSHI/USDT P21_34

**Symbol:** SUSHI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6381 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9093 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -2.6557 |
| sortino_ratio | -0.6954 |
| max_drawdown | 0.5607 |
| cagr | -0.2732 |
| net_avg_win | 61.3026 |
| net_avg_loss | -86.3041 |
| avg_hold_time_bars | 4.7708 |
| exposure | 0.0725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
