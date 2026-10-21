# EMA Hourly Continuation — GMX/USDT P89_200

**Symbol:** GMX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6512 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.8450 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -2.5392 |
| sortino_ratio | -0.6618 |
| max_drawdown | 0.5403 |
| cagr | -0.2626 |
| net_avg_win | 65.2327 |
| net_avg_loss | -83.7525 |
| avg_hold_time_bars | 12.1815 |
| exposure | 0.1860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
