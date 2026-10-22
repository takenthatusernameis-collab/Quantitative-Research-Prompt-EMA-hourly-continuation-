# EMA Hourly Continuation — ILV/USDT P21_34

**Symbol:** ILV/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.5991 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.8718 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -2.8145 |
| sortino_ratio | -0.7523 |
| max_drawdown | 0.5927 |
| cagr | -0.2894 |
| net_avg_win | 52.1736 |
| net_avg_loss | -78.5149 |
| avg_hold_time_bars | 4.8994 |
| exposure | 0.0775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
