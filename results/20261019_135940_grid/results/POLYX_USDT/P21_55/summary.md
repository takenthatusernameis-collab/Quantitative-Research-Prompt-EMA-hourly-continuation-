# EMA Hourly Continuation — POLYX/USDT P21_55

**Symbol:** POLYX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 891 |
| net_profit_factor | 0.5674 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.9601 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -5.8862 |
| sortino_ratio | -2.4783 |
| max_drawdown | 0.9509 |
| cagr | -0.6964 |
| net_avg_win | 30.0915 |
| net_avg_loss | -46.0310 |
| avg_hold_time_bars | 5.8047 |
| exposure | 0.2351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
