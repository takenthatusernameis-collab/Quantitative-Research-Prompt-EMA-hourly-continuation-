# EMA Hourly Continuation — LISTA/USDT P12_50

**Symbol:** LISTA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 890 |
| net_profit_factor | 0.6386 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.9498 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -5.0733 |
| sortino_ratio | -2.2097 |
| max_drawdown | 0.9161 |
| cagr | -0.6500 |
| net_avg_win | 39.2948 |
| net_avg_loss | -52.7933 |
| avg_hold_time_bars | 8.5247 |
| exposure | 0.3710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
