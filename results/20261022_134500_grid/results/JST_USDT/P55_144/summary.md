# EMA Hourly Continuation — JST/USDT P55_144

**Symbol:** JST/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.4062 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.9641 |
| gross_win_rate | 0.5023 |
| sharpe_ratio | -4.9898 |
| sortino_ratio | -1.4535 |
| max_drawdown | 0.8426 |
| cagr | -0.5184 |
| net_avg_win | 29.5301 |
| net_avg_loss | -59.8116 |
| avg_hold_time_bars | 13.9375 |
| exposure | 0.2725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
