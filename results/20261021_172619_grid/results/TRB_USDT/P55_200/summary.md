# EMA Hourly Continuation — TRB/USDT P55_200

**Symbol:** TRB/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.7339 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -1.7097 |
| sortino_ratio | -0.4324 |
| max_drawdown | 0.4181 |
| cagr | -0.1802 |
| net_avg_win | 72.0090 |
| net_avg_loss | -89.2466 |
| avg_hold_time_bars | 23.4543 |
| exposure | 0.3364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
