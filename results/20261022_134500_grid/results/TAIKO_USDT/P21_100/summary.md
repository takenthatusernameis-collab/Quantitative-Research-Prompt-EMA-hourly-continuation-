# EMA Hourly Continuation — TAIKO/USDT P21_100

**Symbol:** TAIKO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.6122 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9444 |
| gross_win_rate | 0.4899 |
| sharpe_ratio | -3.8815 |
| sortino_ratio | -1.3601 |
| max_drawdown | 0.8091 |
| cagr | -0.4834 |
| net_avg_win | 43.5511 |
| net_avg_loss | -66.9422 |
| avg_hold_time_bars | 14.7230 |
| exposure | 0.4187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
