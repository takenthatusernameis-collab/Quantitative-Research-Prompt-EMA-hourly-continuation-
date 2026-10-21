# EMA Hourly Continuation — ETN/USDT P144_200

**Symbol:** ETN/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 143 |
| net_profit_factor | 0.3847 |
| net_win_rate | 0.3217 |
| gross_profit_factor | 0.4949 |
| gross_win_rate | 0.3217 |
| sharpe_ratio | -3.8774 |
| sortino_ratio | -0.7115 |
| max_drawdown | 0.5130 |
| cagr | -0.2836 |
| net_avg_win | 68.4886 |
| net_avg_loss | -84.4191 |
| avg_hold_time_bars | 10.8182 |
| exposure | 0.0840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
