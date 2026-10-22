# EMA Hourly Continuation — DOT/USDT P55_144

**Symbol:** DOT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.5205 |
| net_win_rate | 0.4549 |
| gross_profit_factor | 0.8931 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -4.4193 |
| sortino_ratio | -1.3207 |
| max_drawdown | 0.8158 |
| cagr | -0.4902 |
| net_avg_win | 41.7765 |
| net_avg_loss | -66.9886 |
| avg_hold_time_bars | 10.8026 |
| exposure | 0.2288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
