# EMA Hourly Continuation — OP/USDT P26_34

**Symbol:** OP/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 166 |
| net_profit_factor | 0.5819 |
| net_win_rate | 0.4518 |
| gross_profit_factor | 0.8123 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -2.0936 |
| sortino_ratio | -0.3851 |
| max_drawdown | 0.3633 |
| cagr | -0.1618 |
| net_avg_win | 66.4392 |
| net_avg_loss | -94.1041 |
| avg_hold_time_bars | 4.3133 |
| exposure | 0.0325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
