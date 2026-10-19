# EMA Hourly Continuation — TWT/USDT P12_26

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1505 |
| net_profit_factor | 0.3226 |
| net_win_rate | 0.4060 |
| gross_profit_factor | 0.8595 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -13.2221 |
| sortino_ratio | -7.3326 |
| max_drawdown | 0.9999 |
| cagr | -0.9761 |
| net_avg_win | 7.7951 |
| net_avg_loss | -16.5123 |
| avg_hold_time_bars | 3.0000 |
| exposure | 0.2052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
