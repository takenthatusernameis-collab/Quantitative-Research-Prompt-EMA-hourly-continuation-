# EMA Hourly Continuation — NUM/USDT P8_34

**Symbol:** NUM/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1321 |
| net_profit_factor | 0.3954 |
| net_win_rate | 0.3520 |
| gross_profit_factor | 0.7598 |
| gross_win_rate | 0.3671 |
| sharpe_ratio | -12.5515 |
| sortino_ratio | -6.4051 |
| max_drawdown | 0.9997 |
| cagr | -0.9611 |
| net_avg_win | 14.0618 |
| net_avg_loss | -19.3176 |
| avg_hold_time_bars | 5.5678 |
| exposure | 0.3343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
