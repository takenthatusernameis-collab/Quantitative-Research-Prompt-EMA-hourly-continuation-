# EMA Hourly Continuation — IOST/USDT P12_144

**Symbol:** IOST/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6730 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 1.0253 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -2.5536 |
| sortino_ratio | -0.7476 |
| max_drawdown | 0.6523 |
| cagr | -0.3079 |
| net_avg_win | 56.9377 |
| net_avg_loss | -83.4541 |
| avg_hold_time_bars | 35.3440 |
| exposure | 0.7053 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
