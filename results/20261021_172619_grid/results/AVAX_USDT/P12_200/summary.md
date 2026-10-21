# EMA Hourly Continuation — AVAX/USDT P12_200

**Symbol:** AVAX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.8449 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0011 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.8756 |
| sortino_ratio | -0.2060 |
| max_drawdown | 0.3025 |
| cagr | -0.0920 |
| net_avg_win | 86.9053 |
| net_avg_loss | -102.8555 |
| avg_hold_time_bars | 59.9111 |
| exposure | 0.7353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
