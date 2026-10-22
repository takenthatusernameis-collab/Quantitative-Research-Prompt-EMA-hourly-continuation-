# EMA Hourly Continuation — PEPE/USDT P21_89

**Symbol:** PEPE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.5700 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.8450 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -5.2955 |
| sortino_ratio | -1.9161 |
| max_drawdown | 0.9080 |
| cagr | -0.6069 |
| net_avg_win | 40.6338 |
| net_avg_loss | -56.6802 |
| avg_hold_time_bars | 12.9625 |
| exposure | 0.3924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
