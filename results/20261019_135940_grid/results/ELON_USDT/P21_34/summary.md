# EMA Hourly Continuation — ELON/USDT P21_34

**Symbol:** ELON/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1030 |
| net_profit_factor | 0.3067 |
| net_win_rate | 0.3932 |
| gross_profit_factor | 0.6837 |
| gross_win_rate | 0.4000 |
| sharpe_ratio | -11.3403 |
| sortino_ratio | -5.2531 |
| max_drawdown | 0.9986 |
| cagr | -0.9273 |
| net_avg_win | 10.9058 |
| net_avg_loss | -23.0448 |
| avg_hold_time_bars | 2.6602 |
| exposure | 0.1245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
