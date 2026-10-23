# EMA Hourly Continuation — AURORA/USDT P12_144

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.6311 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9425 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -3.4982 |
| sortino_ratio | -1.0973 |
| max_drawdown | 0.7466 |
| cagr | -0.4113 |
| net_avg_win | 53.7959 |
| net_avg_loss | -74.9819 |
| avg_hold_time_bars | 27.1800 |
| exposure | 0.6177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
