# EMA Hourly Continuation — LPT/USDT P21_144

**Symbol:** LPT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.7583 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9179 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -1.8242 |
| sortino_ratio | -0.5261 |
| max_drawdown | 0.4684 |
| cagr | -0.2158 |
| net_avg_win | 72.7434 |
| net_avg_loss | -88.3147 |
| avg_hold_time_bars | 26.2555 |
| exposure | 0.4905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
