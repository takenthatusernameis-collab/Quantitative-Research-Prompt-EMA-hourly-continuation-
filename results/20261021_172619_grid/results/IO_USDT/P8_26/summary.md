# EMA Hourly Continuation — IO/USDT P8_26

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.7409 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9233 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -2.5791 |
| sortino_ratio | -0.9631 |
| max_drawdown | 0.6670 |
| cagr | -0.3573 |
| net_avg_win | 60.1140 |
| net_avg_loss | -74.5936 |
| avg_hold_time_bars | 6.1680 |
| exposure | 0.1920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
