# EMA Hourly Continuation — CTC/USDT P12_55

**Symbol:** CTC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1035 |
| net_profit_factor | 0.5356 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.9618 |
| gross_win_rate | 0.4802 |
| sharpe_ratio | -6.4423 |
| sortino_ratio | -2.9261 |
| max_drawdown | 0.9732 |
| cagr | -0.7573 |
| net_avg_win | 23.4910 |
| net_avg_loss | -37.4905 |
| avg_hold_time_bars | 8.5546 |
| exposure | 0.4025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
