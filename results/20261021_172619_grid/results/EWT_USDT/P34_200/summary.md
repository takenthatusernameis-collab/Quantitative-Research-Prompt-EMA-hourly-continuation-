# EMA Hourly Continuation — EWT/USDT P34_200

**Symbol:** EWT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.8202 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9702 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -1.0791 |
| sortino_ratio | -0.2815 |
| max_drawdown | 0.3602 |
| cagr | -0.1231 |
| net_avg_win | 77.6640 |
| net_avg_loss | -93.0032 |
| avg_hold_time_bars | 25.5435 |
| exposure | 0.3866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
