# EMA Hourly Continuation — FLUX/USDT P8_89

**Symbol:** FLUX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.8243 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 0.9959 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -1.2937 |
| sortino_ratio | -0.4263 |
| max_drawdown | 0.4710 |
| cagr | -0.1806 |
| net_avg_win | 69.4294 |
| net_avg_loss | -85.1889 |
| avg_hold_time_bars | 26.0435 |
| exposure | 0.6262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
