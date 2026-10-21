# EMA Hourly Continuation — ETHFI/USDT P100_144

**Symbol:** ETHFI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.8315 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0536 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -0.9082 |
| sortino_ratio | -0.2015 |
| max_drawdown | 0.2581 |
| cagr | -0.0895 |
| net_avg_win | 84.8597 |
| net_avg_loss | -107.3361 |
| avg_hold_time_bars | 6.2269 |
| exposure | 0.0674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
