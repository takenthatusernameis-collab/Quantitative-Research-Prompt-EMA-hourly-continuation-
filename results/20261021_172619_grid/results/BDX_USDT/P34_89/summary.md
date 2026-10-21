# EMA Hourly Continuation — BDX/USDT P34_89

**Symbol:** BDX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.4954 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.7897 |
| gross_win_rate | 0.4411 |
| sharpe_ratio | -3.9565 |
| sortino_ratio | -1.0312 |
| max_drawdown | 0.7133 |
| cagr | -0.3804 |
| net_avg_win | 47.0335 |
| net_avg_loss | -74.9269 |
| avg_hold_time_bars | 8.3535 |
| exposure | 0.1257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
