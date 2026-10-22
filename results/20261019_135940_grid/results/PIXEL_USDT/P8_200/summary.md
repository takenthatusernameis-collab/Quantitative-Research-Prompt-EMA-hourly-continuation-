# EMA Hourly Continuation — PIXEL/USDT P8_200

**Symbol:** PIXEL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.8038 |
| net_win_rate | 0.5100 |
| gross_profit_factor | 1.0556 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -1.2386 |
| sortino_ratio | -0.2979 |
| max_drawdown | 0.3683 |
| cagr | -0.1374 |
| net_avg_win | 83.3096 |
| net_avg_loss | -107.8798 |
| avg_hold_time_bars | 61.8933 |
| exposure | 0.8402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
