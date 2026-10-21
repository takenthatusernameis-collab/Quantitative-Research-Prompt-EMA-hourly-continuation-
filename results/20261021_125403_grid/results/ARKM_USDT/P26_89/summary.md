# EMA Hourly Continuation — ARKM/USDT P26_89

**Symbol:** ARKM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.7435 |
| net_win_rate | 0.4721 |
| gross_profit_factor | 0.9094 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -2.1713 |
| sortino_ratio | -0.6673 |
| max_drawdown | 0.5562 |
| cagr | -0.2650 |
| net_avg_win | 70.9322 |
| net_avg_loss | -85.3223 |
| avg_hold_time_bars | 13.0193 |
| exposure | 0.2758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
