# EMA Hourly Continuation — AR/USDT P12_200

**Symbol:** AR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.7899 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9658 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -1.1829 |
| sortino_ratio | -0.2652 |
| max_drawdown | 0.2984 |
| cagr | -0.1169 |
| net_avg_win | 82.6280 |
| net_avg_loss | -100.4828 |
| avg_hold_time_bars | 72.9920 |
| exposure | 0.8261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
