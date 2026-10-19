# EMA Hourly Continuation — KAS/USDT P8_200

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6803 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9993 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -2.9259 |
| sortino_ratio | -0.8479 |
| max_drawdown | 0.6749 |
| cagr | -0.3447 |
| net_avg_win | 64.7392 |
| net_avg_loss | -91.7487 |
| avg_hold_time_bars | 39.9635 |
| exposure | 0.7956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
