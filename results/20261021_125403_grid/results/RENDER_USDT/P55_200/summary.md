# EMA Hourly Continuation — RENDER/USDT P55_200

**Symbol:** RENDER/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.9534 |
| net_win_rate | 0.5353 |
| gross_profit_factor | 1.1435 |
| gross_win_rate | 0.5353 |
| sharpe_ratio | -0.2075 |
| sortino_ratio | -0.0502 |
| max_drawdown | 0.1592 |
| cagr | -0.0271 |
| net_avg_win | 91.6296 |
| net_avg_loss | -110.6943 |
| avg_hold_time_bars | 28.4481 |
| exposure | 0.3619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
