# EMA Hourly Continuation — XEC/USDT P34_200

**Symbol:** XEC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6474 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9639 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -3.0792 |
| sortino_ratio | -0.9053 |
| max_drawdown | 0.6798 |
| cagr | -0.3526 |
| net_avg_win | 57.9586 |
| net_avg_loss | -82.8493 |
| avg_hold_time_bars | 25.4465 |
| exposure | 0.5055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
