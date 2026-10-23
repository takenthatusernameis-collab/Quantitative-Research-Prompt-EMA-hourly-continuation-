# EMA Hourly Continuation — UQC/USDT P34_144

**Symbol:** UQC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.2407 |
| net_win_rate | 0.2710 |
| gross_profit_factor | 0.3719 |
| gross_win_rate | 0.2748 |
| sharpe_ratio | -6.2449 |
| sortino_ratio | -1.4194 |
| max_drawdown | 0.8294 |
| cagr | -0.5040 |
| net_avg_win | 37.0209 |
| net_avg_loss | -57.1847 |
| avg_hold_time_bars | 51.4389 |
| exposure | 0.6100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
