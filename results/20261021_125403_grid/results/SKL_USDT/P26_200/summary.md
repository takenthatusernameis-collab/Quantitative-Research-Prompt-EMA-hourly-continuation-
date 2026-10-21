# EMA Hourly Continuation — SKL/USDT P26_200

**Symbol:** SKL/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.8520 |
| net_win_rate | 0.5019 |
| gross_profit_factor | 0.9921 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -0.7602 |
| sortino_ratio | -0.1772 |
| max_drawdown | 0.3051 |
| cagr | -0.0802 |
| net_avg_win | 81.9929 |
| net_avg_loss | -96.9644 |
| avg_hold_time_bars | 50.8906 |
| exposure | 0.6130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
