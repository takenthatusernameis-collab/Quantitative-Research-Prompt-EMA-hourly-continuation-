# EMA Hourly Continuation — ALT/USDT P20_144

**Symbol:** ALT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6431 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.8364 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -2.9542 |
| sortino_ratio | -0.8826 |
| max_drawdown | 0.6618 |
| cagr | -0.3386 |
| net_avg_win | 57.0626 |
| net_avg_loss | -74.1792 |
| avg_hold_time_bars | 29.1406 |
| exposure | 0.5934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
