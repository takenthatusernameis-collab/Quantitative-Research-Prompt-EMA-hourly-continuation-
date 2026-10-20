# EMA Hourly Continuation — RSR/USDT P20_200

**Symbol:** RSR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.6866 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.9216 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -2.6104 |
| sortino_ratio | -0.7400 |
| max_drawdown | 0.5959 |
| cagr | -0.3004 |
| net_avg_win | 67.9348 |
| net_avg_loss | -86.2922 |
| avg_hold_time_bars | 32.9610 |
| exposure | 0.6143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
