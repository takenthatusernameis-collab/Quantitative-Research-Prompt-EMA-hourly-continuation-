# EMA Hourly Continuation — IO/USDT P34_144

**Symbol:** IO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.6587 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.9065 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -3.1057 |
| sortino_ratio | -1.0083 |
| max_drawdown | 0.6921 |
| cagr | -0.3849 |
| net_avg_win | 55.0684 |
| net_avg_loss | -75.4026 |
| avg_hold_time_bars | 14.5734 |
| exposure | 0.3556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
