# EMA Hourly Continuation — CYBER/USDT P12_144

**Symbol:** CYBER/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.8719 |
| net_win_rate | 0.5079 |
| gross_profit_factor | 1.0366 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -0.8851 |
| sortino_ratio | -0.2467 |
| max_drawdown | 0.3703 |
| cagr | -0.1101 |
| net_avg_win | 90.0401 |
| net_avg_loss | -106.6020 |
| avg_hold_time_bars | 39.5503 |
| exposure | 0.6795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
