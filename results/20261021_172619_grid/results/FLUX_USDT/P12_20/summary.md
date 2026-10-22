# EMA Hourly Continuation — FLUX/USDT P12_20

**Symbol:** FLUX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.6936 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9401 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -1.8550 |
| sortino_ratio | -0.4409 |
| max_drawdown | 0.4403 |
| cagr | -0.1825 |
| net_avg_win | 67.1010 |
| net_avg_loss | -91.9367 |
| avg_hold_time_bars | 5.0764 |
| exposure | 0.0635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
