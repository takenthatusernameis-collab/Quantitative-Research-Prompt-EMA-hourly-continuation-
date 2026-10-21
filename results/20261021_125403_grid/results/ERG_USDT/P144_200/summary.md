# EMA Hourly Continuation — ERG/USDT P144_200

**Symbol:** ERG/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 178 |
| net_profit_factor | 0.4901 |
| net_win_rate | 0.4101 |
| gross_profit_factor | 0.6938 |
| gross_win_rate | 0.4101 |
| sharpe_ratio | -2.9222 |
| sortino_ratio | -0.5553 |
| max_drawdown | 0.4979 |
| cagr | -0.2264 |
| net_avg_win | 62.5467 |
| net_avg_loss | -88.7331 |
| avg_hold_time_bars | 7.1236 |
| exposure | 0.0576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
