# EMA Hourly Continuation — TIA/USDT P144_200

**Symbol:** TIA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 170 |
| net_profit_factor | 0.6557 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.8262 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -1.7110 |
| sortino_ratio | -0.3171 |
| max_drawdown | 0.3187 |
| cagr | -0.1356 |
| net_avg_win | 75.8007 |
| net_avg_loss | -95.7097 |
| avg_hold_time_bars | 7.4824 |
| exposure | 0.0578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
