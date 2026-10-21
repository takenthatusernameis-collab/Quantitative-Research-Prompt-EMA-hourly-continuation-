# EMA Hourly Continuation — ZRX/USDT P21_200

**Symbol:** ZRX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.8187 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0049 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.1250 |
| sortino_ratio | -0.2899 |
| max_drawdown | 0.3208 |
| cagr | -0.1268 |
| net_avg_win | 79.9452 |
| net_avg_loss | -98.2467 |
| avg_hold_time_bars | 41.4031 |
| exposure | 0.6116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
