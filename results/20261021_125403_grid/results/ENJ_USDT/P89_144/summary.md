# EMA Hourly Continuation — ENJ/USDT P89_144

**Symbol:** ENJ/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.6997 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.9190 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -1.9848 |
| sortino_ratio | -0.4603 |
| max_drawdown | 0.4605 |
| cagr | -0.1909 |
| net_avg_win | 77.1672 |
| net_avg_loss | -98.4675 |
| avg_hold_time_bars | 8.5925 |
| exposure | 0.1030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
