# EMA Hourly Continuation — XPR/USDT P50_200

**Symbol:** XPR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.7940 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9792 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.1212 |
| sortino_ratio | -0.2716 |
| max_drawdown | 0.3054 |
| cagr | -0.1181 |
| net_avg_win | 72.9259 |
| net_avg_loss | -91.8492 |
| avg_hold_time_bars | 24.6538 |
| exposure | 0.3205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
