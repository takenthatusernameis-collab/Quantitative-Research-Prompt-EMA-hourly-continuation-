# EMA Hourly Continuation — ILV/USDT P21_26

**Symbol:** ILV/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 212 |
| net_profit_factor | 0.6684 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0076 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -1.6987 |
| sortino_ratio | -0.3561 |
| max_drawdown | 0.3598 |
| cagr | -0.1493 |
| net_avg_win | 62.2820 |
| net_avg_loss | -96.7586 |
| avg_hold_time_bars | 5.0283 |
| exposure | 0.0485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
