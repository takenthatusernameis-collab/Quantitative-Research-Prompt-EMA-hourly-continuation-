# EMA Hourly Continuation — TWT/USDT P8_200

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.8890 |
| net_win_rate | 0.5256 |
| gross_profit_factor | 1.0985 |
| gross_win_rate | 0.5256 |
| sharpe_ratio | -0.5566 |
| sortino_ratio | -0.1372 |
| max_drawdown | 0.2990 |
| cagr | -0.0639 |
| net_avg_win | 79.5209 |
| net_avg_loss | -99.1027 |
| avg_hold_time_bars | 60.5154 |
| exposure | 0.8060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
