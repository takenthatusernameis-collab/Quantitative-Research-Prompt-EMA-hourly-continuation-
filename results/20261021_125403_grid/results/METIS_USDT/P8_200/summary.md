# EMA Hourly Continuation — METIS/USDT P8_200

**Symbol:** METIS/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.8367 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9721 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -0.9193 |
| sortino_ratio | -0.2125 |
| max_drawdown | 0.2777 |
| cagr | -0.0948 |
| net_avg_win | 87.2100 |
| net_avg_loss | -101.8823 |
| avg_hold_time_bars | 67.7224 |
| exposure | 0.8096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
