# EMA Hourly Continuation — APT/USDT P89_144

**Symbol:** APT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.8859 |
| net_win_rate | 0.5409 |
| gross_profit_factor | 1.1749 |
| gross_win_rate | 0.5409 |
| sharpe_ratio | -0.5895 |
| sortino_ratio | -0.1369 |
| max_drawdown | 0.2402 |
| cagr | -0.0628 |
| net_avg_win | 83.9970 |
| net_avg_loss | -111.6839 |
| avg_hold_time_bars | 7.4008 |
| exposure | 0.0865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
