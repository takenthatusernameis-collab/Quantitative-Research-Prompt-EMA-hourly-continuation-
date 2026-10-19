# EMA Hourly Continuation — AXS/USDT P12_21

**Symbol:** AXS/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1402 |
| net_profit_factor | 0.2076 |
| net_win_rate | 0.4073 |
| gross_profit_factor | 0.6232 |
| gross_win_rate | 0.4544 |
| sharpe_ratio | -12.9194 |
| sortino_ratio | -6.9347 |
| max_drawdown | 0.9999 |
| cagr | -0.9705 |
| net_avg_win | 4.5890 |
| net_avg_loss | -15.1852 |
| avg_hold_time_bars | 2.3217 |
| exposure | 0.1473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
