# EMA Hourly Continuation — FIDA/USDT P89_200

**Symbol:** FIDA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.5846 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.8420 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -3.5273 |
| sortino_ratio | -1.0426 |
| max_drawdown | 0.7168 |
| cagr | -0.3858 |
| net_avg_win | 50.8083 |
| net_avg_loss | -70.9763 |
| avg_hold_time_bars | 10.8165 |
| exposure | 0.2134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
