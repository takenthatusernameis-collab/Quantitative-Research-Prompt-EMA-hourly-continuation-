# EMA Hourly Continuation — COMP/USDT P12_144

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.7381 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9489 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -1.7057 |
| sortino_ratio | -0.4777 |
| max_drawdown | 0.4611 |
| cagr | -0.1975 |
| net_avg_win | 63.2807 |
| net_avg_loss | -82.6772 |
| avg_hold_time_bars | 40.4831 |
| exposure | 0.7085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
