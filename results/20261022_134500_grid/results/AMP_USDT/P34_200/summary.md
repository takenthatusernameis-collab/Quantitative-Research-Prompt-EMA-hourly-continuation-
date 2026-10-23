# EMA Hourly Continuation — AMP/USDT P34_200

**Symbol:** AMP/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.4304 |
| net_win_rate | 0.4148 |
| gross_profit_factor | 0.6900 |
| gross_win_rate | 0.4233 |
| sharpe_ratio | -5.6352 |
| sortino_ratio | -1.9290 |
| max_drawdown | 0.9089 |
| cagr | -0.6022 |
| net_avg_win | 27.6823 |
| net_avg_loss | -45.5966 |
| avg_hold_time_bars | 19.2850 |
| exposure | 0.5198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
