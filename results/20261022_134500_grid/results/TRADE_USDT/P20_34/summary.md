# EMA Hourly Continuation — TRADE/USDT P20_34

**Symbol:** TRADE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 908 |
| net_profit_factor | 0.3713 |
| net_win_rate | 0.3800 |
| gross_profit_factor | 0.7195 |
| gross_win_rate | 0.3943 |
| sharpe_ratio | -9.8943 |
| sortino_ratio | -4.2311 |
| max_drawdown | 0.9956 |
| cagr | -0.8831 |
| net_avg_win | 17.0395 |
| net_avg_loss | -28.1226 |
| avg_hold_time_bars | 3.5055 |
| exposure | 0.1447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
