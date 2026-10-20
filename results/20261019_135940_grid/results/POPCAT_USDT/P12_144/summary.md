# EMA Hourly Continuation — POPCAT/USDT P12_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.7079 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.9187 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.4548 |
| sortino_ratio | -0.7585 |
| max_drawdown | 0.5748 |
| cagr | -0.3059 |
| net_avg_win | 66.1273 |
| net_avg_loss | -84.9222 |
| avg_hold_time_bars | 30.5476 |
| exposure | 0.6778 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
