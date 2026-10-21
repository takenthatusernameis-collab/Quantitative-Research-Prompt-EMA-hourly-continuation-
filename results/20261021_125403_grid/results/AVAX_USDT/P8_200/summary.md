# EMA Hourly Continuation — AVAX/USDT P8_200

**Symbol:** AVAX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.8977 |
| net_win_rate | 0.5153 |
| gross_profit_factor | 1.0578 |
| gross_win_rate | 0.5153 |
| sharpe_ratio | -0.5206 |
| sortino_ratio | -0.1211 |
| max_drawdown | 0.2345 |
| cagr | -0.0569 |
| net_avg_win | 89.0068 |
| net_avg_loss | -105.3945 |
| avg_hold_time_bars | 67.3779 |
| exposure | 0.8024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
