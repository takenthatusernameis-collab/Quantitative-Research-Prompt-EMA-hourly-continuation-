# EMA Hourly Continuation — EWT/USDT P8_21

**Symbol:** EWT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1476 |
| net_profit_factor | 0.2923 |
| net_win_rate | 0.3496 |
| gross_profit_factor | 0.5945 |
| gross_win_rate | 0.3794 |
| sharpe_ratio | -15.0648 |
| sortino_ratio | -8.2428 |
| max_drawdown | 1.0000 |
| cagr | -0.9871 |
| net_avg_win | 8.0049 |
| net_avg_loss | -14.7191 |
| avg_hold_time_bars | 3.2785 |
| exposure | 0.2200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
