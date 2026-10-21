# EMA Hourly Continuation — SUI/USDT P89_200

**Symbol:** SUI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.6889 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.8618 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -1.7411 |
| sortino_ratio | -0.3931 |
| max_drawdown | 0.3836 |
| cagr | -0.1650 |
| net_avg_win | 68.3356 |
| net_avg_loss | -87.3544 |
| avg_hold_time_bars | 14.3214 |
| exposure | 0.1640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
