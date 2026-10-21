# EMA Hourly Continuation — SHIB/USDT P12_55

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.7336 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9781 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -2.4904 |
| sortino_ratio | -0.8766 |
| max_drawdown | 0.6657 |
| cagr | -0.3310 |
| net_avg_win | 58.7506 |
| net_avg_loss | -77.9869 |
| avg_hold_time_bars | 11.2980 |
| exposure | 0.3102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
