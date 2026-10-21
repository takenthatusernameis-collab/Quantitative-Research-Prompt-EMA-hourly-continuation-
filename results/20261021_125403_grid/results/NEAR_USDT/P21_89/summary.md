# EMA Hourly Continuation — NEAR/USDT P21_89

**Symbol:** NEAR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.8000 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9684 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -1.4956 |
| sortino_ratio | -0.4499 |
| max_drawdown | 0.4654 |
| cagr | -0.1884 |
| net_avg_win | 74.8772 |
| net_avg_loss | -90.6808 |
| avg_hold_time_bars | 17.8059 |
| exposure | 0.3585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
