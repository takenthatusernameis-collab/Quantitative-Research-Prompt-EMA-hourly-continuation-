# EMA Hourly Continuation — GMX/USDT P26_144

**Symbol:** GMX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.6315 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.9182 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -3.7374 |
| sortino_ratio | -1.2637 |
| max_drawdown | 0.7893 |
| cagr | -0.4492 |
| net_avg_win | 50.0179 |
| net_avg_loss | -67.9633 |
| avg_hold_time_bars | 16.2292 |
| exposure | 0.4249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
