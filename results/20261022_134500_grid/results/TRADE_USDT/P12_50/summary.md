# EMA Hourly Continuation — TRADE/USDT P12_50

**Symbol:** TRADE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 901 |
| net_profit_factor | 0.6072 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.9213 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -5.8361 |
| sortino_ratio | -2.4470 |
| max_drawdown | 0.9543 |
| cagr | -0.7011 |
| net_avg_win | 36.3360 |
| net_avg_loss | -48.8597 |
| avg_hold_time_bars | 8.3896 |
| exposure | 0.3436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
