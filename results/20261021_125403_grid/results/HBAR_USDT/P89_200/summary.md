# EMA Hourly Continuation — HBAR/USDT P89_200

**Symbol:** HBAR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.8079 |
| net_win_rate | 0.5110 |
| gross_profit_factor | 1.0394 |
| gross_win_rate | 0.5110 |
| sharpe_ratio | -1.1287 |
| sortino_ratio | -0.2671 |
| max_drawdown | 0.3572 |
| cagr | -0.1163 |
| net_avg_win | 80.7419 |
| net_avg_loss | -104.4503 |
| avg_hold_time_bars | 17.4596 |
| exposure | 0.2159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
