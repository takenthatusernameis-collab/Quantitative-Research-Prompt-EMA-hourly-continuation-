# EMA Hourly Continuation — TNSR/USDT P100_144

**Symbol:** TNSR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.8012 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0854 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -1.1939 |
| sortino_ratio | -0.2843 |
| max_drawdown | 0.3215 |
| cagr | -0.1231 |
| net_avg_win | 79.5019 |
| net_avg_loss | -107.4997 |
| avg_hold_time_bars | 6.4655 |
| exposure | 0.0805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
