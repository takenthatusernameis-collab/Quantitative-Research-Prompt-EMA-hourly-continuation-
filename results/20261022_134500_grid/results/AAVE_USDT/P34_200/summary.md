# EMA Hourly Continuation — AAVE/USDT P34_200

**Symbol:** AAVE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6812 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 1.0200 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -2.6038 |
| sortino_ratio | -0.7486 |
| max_drawdown | 0.6254 |
| cagr | -0.3054 |
| net_avg_win | 61.2997 |
| net_avg_loss | -87.8860 |
| avg_hold_time_bars | 24.1868 |
| exposure | 0.4650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
