# EMA Hourly Continuation — LQTY/USDT P21_89

**Symbol:** LQTY/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.7313 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9184 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -2.2228 |
| sortino_ratio | -0.7069 |
| max_drawdown | 0.5755 |
| cagr | -0.2784 |
| net_avg_win | 63.6024 |
| net_avg_loss | -80.2813 |
| avg_hold_time_bars | 17.7680 |
| exposure | 0.4020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
