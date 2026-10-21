# EMA Hourly Continuation — TRB/USDT P26_89

**Symbol:** TRB/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6635 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.8512 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -2.6865 |
| sortino_ratio | -0.7955 |
| max_drawdown | 0.6106 |
| cagr | -0.3058 |
| net_avg_win | 59.0175 |
| net_avg_loss | -76.4091 |
| avg_hold_time_bars | 15.9678 |
| exposure | 0.3143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
