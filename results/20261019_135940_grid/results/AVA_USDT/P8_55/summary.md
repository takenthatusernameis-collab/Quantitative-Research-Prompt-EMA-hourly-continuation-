# EMA Hourly Continuation — AVA/USDT P8_55

**Symbol:** AVA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1018 |
| net_profit_factor | 0.5360 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8411 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -6.0881 |
| sortino_ratio | -2.7287 |
| max_drawdown | 0.9687 |
| cagr | -0.7331 |
| net_avg_win | 23.8420 |
| net_avg_loss | -37.6983 |
| avg_hold_time_bars | 10.2574 |
| exposure | 0.4746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
