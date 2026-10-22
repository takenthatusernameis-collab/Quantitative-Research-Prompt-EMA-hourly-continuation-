# EMA Hourly Continuation — HBAR/USDT P89_200

**Symbol:** HBAR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6230 |
| net_win_rate | 0.4883 |
| gross_profit_factor | 0.9953 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -3.1634 |
| sortino_ratio | -0.8664 |
| max_drawdown | 0.6663 |
| cagr | -0.3470 |
| net_avg_win | 57.7538 |
| net_avg_loss | -88.4673 |
| avg_hold_time_bars | 12.7896 |
| exposure | 0.2238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
