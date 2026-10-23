# EMA Hourly Continuation — FLOW/USDT P8_50

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1143 |
| net_profit_factor | 0.5225 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.9003 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -6.9105 |
| sortino_ratio | -3.2866 |
| max_drawdown | 0.9821 |
| cagr | -0.7964 |
| net_avg_win | 20.6985 |
| net_avg_loss | -32.9468 |
| avg_hold_time_bars | 9.1076 |
| exposure | 0.4732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
