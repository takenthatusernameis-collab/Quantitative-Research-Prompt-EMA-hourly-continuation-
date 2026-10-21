# EMA Hourly Continuation — CVX/USDT P21_200

**Symbol:** CVX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.8905 |
| net_win_rate | 0.5062 |
| gross_profit_factor | 1.0193 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -0.5414 |
| sortino_ratio | -0.1204 |
| max_drawdown | 0.1820 |
| cagr | -0.0564 |
| net_avg_win | 90.4202 |
| net_avg_loss | -104.0976 |
| avg_hold_time_bars | 62.5187 |
| exposure | 0.6849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
