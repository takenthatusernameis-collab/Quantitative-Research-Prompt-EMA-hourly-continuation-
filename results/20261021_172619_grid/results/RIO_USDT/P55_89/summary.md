# EMA Hourly Continuation — RIO/USDT P55_89

**Symbol:** RIO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.6298 |
| net_win_rate | 0.4229 |
| gross_profit_factor | 0.7492 |
| gross_win_rate | 0.4229 |
| sharpe_ratio | -2.5442 |
| sortino_ratio | -0.6025 |
| max_drawdown | 0.5111 |
| cagr | -0.2427 |
| net_avg_win | 71.9286 |
| net_avg_loss | -83.7099 |
| avg_hold_time_bars | 6.0932 |
| exposure | 0.0780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
