# EMA Hourly Continuation — ZBCN/USDT P8_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.8265 |
| net_win_rate | 0.5225 |
| gross_profit_factor | 1.0918 |
| gross_win_rate | 0.5225 |
| sharpe_ratio | -1.4645 |
| sortino_ratio | -0.4997 |
| max_drawdown | 0.4919 |
| cagr | -0.2164 |
| net_avg_win | 71.3162 |
| net_avg_loss | -94.4173 |
| avg_hold_time_bars | 27.6125 |
| exposure | 0.7384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
