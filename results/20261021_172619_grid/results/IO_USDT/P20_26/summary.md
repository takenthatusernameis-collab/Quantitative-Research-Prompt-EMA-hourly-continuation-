# EMA Hourly Continuation — IO/USDT P20_26

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 157 |
| net_profit_factor | 0.6389 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.8152 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -1.8774 |
| sortino_ratio | -0.3449 |
| max_drawdown | 0.3403 |
| cagr | -0.1467 |
| net_avg_win | 78.9016 |
| net_avg_loss | -99.3588 |
| avg_hold_time_bars | 4.8153 |
| exposure | 0.0366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
