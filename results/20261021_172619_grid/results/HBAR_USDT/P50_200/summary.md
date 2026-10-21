# EMA Hourly Continuation — HBAR/USDT P50_200

**Symbol:** HBAR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.8033 |
| net_win_rate | 0.5018 |
| gross_profit_factor | 0.9910 |
| gross_win_rate | 0.5018 |
| sharpe_ratio | -1.1075 |
| sortino_ratio | -0.2657 |
| max_drawdown | 0.3014 |
| cagr | -0.1158 |
| net_avg_win | 76.9689 |
| net_avg_loss | -96.5027 |
| avg_hold_time_bars | 28.9431 |
| exposure | 0.3697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
