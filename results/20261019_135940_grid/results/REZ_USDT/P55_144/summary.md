# EMA Hourly Continuation — REZ/USDT P55_144

**Symbol:** REZ/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7185 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9885 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -2.3879 |
| sortino_ratio | -0.7264 |
| max_drawdown | 0.6063 |
| cagr | -0.2914 |
| net_avg_win | 65.6569 |
| net_avg_loss | -87.8301 |
| avg_hold_time_bars | 13.0879 |
| exposure | 0.2747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
