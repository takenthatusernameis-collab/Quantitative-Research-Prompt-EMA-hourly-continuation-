# EMA Hourly Continuation — CARV/USDT P21_34

**Symbol:** CARV/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 781 |
| net_profit_factor | 0.3916 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.8712 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -8.1258 |
| sortino_ratio | -3.5601 |
| max_drawdown | 0.9736 |
| cagr | -0.8324 |
| net_avg_win | 18.0509 |
| net_avg_loss | -36.8590 |
| avg_hold_time_bars | 4.1037 |
| exposure | 0.1804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
