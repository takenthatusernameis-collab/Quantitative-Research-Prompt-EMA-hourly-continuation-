# EMA Hourly Continuation — PUNDIX/USDT P89_200

**Symbol:** PUNDIX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.5663 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9794 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -3.4472 |
| sortino_ratio | -0.9709 |
| max_drawdown | 0.6896 |
| cagr | -0.3724 |
| net_avg_win | 47.1339 |
| net_avg_loss | -76.0676 |
| avg_hold_time_bars | 13.5625 |
| exposure | 0.2466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
