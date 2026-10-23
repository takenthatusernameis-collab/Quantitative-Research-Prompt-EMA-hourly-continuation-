# EMA Hourly Continuation — CHR/USDT P20_34

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1125 |
| net_profit_factor | 0.3716 |
| net_win_rate | 0.4133 |
| gross_profit_factor | 0.8068 |
| gross_win_rate | 0.4409 |
| sharpe_ratio | -9.7442 |
| sortino_ratio | -4.6153 |
| max_drawdown | 0.9970 |
| cagr | -0.8994 |
| net_avg_win | 12.6792 |
| net_avg_loss | -24.0384 |
| avg_hold_time_bars | 3.0053 |
| exposure | 0.1530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
