# EMA Hourly Continuation — PEPE/USDT P55_200

**Symbol:** PEPE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.6615 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9275 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -2.7181 |
| sortino_ratio | -0.7678 |
| max_drawdown | 0.6082 |
| cagr | -0.3049 |
| net_avg_win | 61.5943 |
| net_avg_loss | -84.2441 |
| avg_hold_time_bars | 20.7625 |
| exposure | 0.3775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
