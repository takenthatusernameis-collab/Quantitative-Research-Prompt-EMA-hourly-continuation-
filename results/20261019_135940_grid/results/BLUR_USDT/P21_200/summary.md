# EMA Hourly Continuation — BLUR/USDT P21_200

**Symbol:** BLUR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.7557 |
| net_win_rate | 0.5141 |
| gross_profit_factor | 1.0520 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -1.5795 |
| sortino_ratio | -0.4193 |
| max_drawdown | 0.4265 |
| cagr | -0.1816 |
| net_avg_win | 67.4445 |
| net_avg_loss | -94.4317 |
| avg_hold_time_bars | 42.8701 |
| exposure | 0.6867 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
