# EMA Hourly Continuation — HBAR/USDT P26_200

**Symbol:** HBAR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.7413 |
| net_win_rate | 0.5150 |
| gross_profit_factor | 1.0723 |
| gross_win_rate | 0.5177 |
| sharpe_ratio | -1.9016 |
| sortino_ratio | -0.5095 |
| max_drawdown | 0.5181 |
| cagr | -0.2202 |
| net_avg_win | 70.4057 |
| net_avg_loss | -100.8491 |
| avg_hold_time_bars | 34.4414 |
| exposure | 0.5745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
