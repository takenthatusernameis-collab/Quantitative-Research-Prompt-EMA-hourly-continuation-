# EMA Hourly Continuation — BAT/USDT P55_89

**Symbol:** BAT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.6554 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9798 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.4005 |
| sortino_ratio | -0.6656 |
| max_drawdown | 0.5594 |
| cagr | -0.2618 |
| net_avg_win | 54.5319 |
| net_avg_loss | -83.2074 |
| avg_hold_time_bars | 5.7151 |
| exposure | 0.0966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
