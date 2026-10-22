# EMA Hourly Continuation — ETHFI/USDT P34_100

**Symbol:** ETHFI/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.6834 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9936 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -3.4268 |
| sortino_ratio | -1.2557 |
| max_drawdown | 0.7850 |
| cagr | -0.4497 |
| net_avg_win | 51.2754 |
| net_avg_loss | -70.5046 |
| avg_hold_time_bars | 9.5274 |
| exposure | 0.2923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
