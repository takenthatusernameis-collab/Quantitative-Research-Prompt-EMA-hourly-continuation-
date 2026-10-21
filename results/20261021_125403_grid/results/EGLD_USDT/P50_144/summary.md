# EMA Hourly Continuation — EGLD/USDT P50_144

**Symbol:** EGLD/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7338 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9479 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -1.6935 |
| sortino_ratio | -0.4434 |
| max_drawdown | 0.4123 |
| cagr | -0.1844 |
| net_avg_win | 67.3422 |
| net_avg_loss | -88.0179 |
| avg_hold_time_bars | 18.9104 |
| exposure | 0.2880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
