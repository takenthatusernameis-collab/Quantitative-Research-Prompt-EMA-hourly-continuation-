# EMA Hourly Continuation — GLM/USDT P26_144

**Symbol:** GLM/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.5874 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.8875 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -3.7471 |
| sortino_ratio | -1.2386 |
| max_drawdown | 0.7748 |
| cagr | -0.4446 |
| net_avg_win | 42.9054 |
| net_avg_loss | -63.6056 |
| avg_hold_time_bars | 18.0909 |
| exposure | 0.4523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
