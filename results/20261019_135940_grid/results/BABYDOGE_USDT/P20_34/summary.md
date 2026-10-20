# EMA Hourly Continuation — BABYDOGE/USDT P20_34

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 20 |
| net_profit_factor | 0.9136 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9912 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.1150 |
| sortino_ratio | -0.0073 |
| max_drawdown | 0.0362 |
| cagr | -0.0036 |
| net_avg_win | 96.8142 |
| net_avg_loss | -105.9712 |
| avg_hold_time_bars | 12.4500 |
| exposure | 0.0113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
