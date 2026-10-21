# EMA Hourly Continuation — GLM/USDT P26_144

**Symbol:** GLM/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7229 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9452 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -2.0513 |
| sortino_ratio | -0.6101 |
| max_drawdown | 0.5149 |
| cagr | -0.2459 |
| net_avg_win | 62.1936 |
| net_avg_loss | -82.5423 |
| avg_hold_time_bars | 22.3862 |
| exposure | 0.4426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
