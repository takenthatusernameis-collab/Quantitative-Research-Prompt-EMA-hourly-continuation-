# EMA Hourly Continuation — CELO/USDT P21_34

**Symbol:** CELO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1113 |
| net_profit_factor | 0.3159 |
| net_win_rate | 0.4169 |
| gross_profit_factor | 0.6858 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -10.4059 |
| sortino_ratio | -4.9037 |
| max_drawdown | 0.9982 |
| cagr | -0.9182 |
| net_avg_win | 9.9355 |
| net_avg_loss | -22.4838 |
| avg_hold_time_bars | 2.8886 |
| exposure | 0.1455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
