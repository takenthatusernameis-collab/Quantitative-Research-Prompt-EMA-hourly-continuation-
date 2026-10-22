# EMA Hourly Continuation — BAND/USDT P12_144

**Symbol:** BAND/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.8102 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0117 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5094 |
| sortino_ratio | -0.4359 |
| max_drawdown | 0.4972 |
| cagr | -0.1834 |
| net_avg_win | 82.9078 |
| net_avg_loss | -102.3360 |
| avg_hold_time_bars | 35.3835 |
| exposure | 0.6597 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
