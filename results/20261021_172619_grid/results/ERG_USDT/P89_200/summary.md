# EMA Hourly Continuation — ERG/USDT P89_200

**Symbol:** ERG/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.5599 |
| net_win_rate | 0.4275 |
| gross_profit_factor | 0.7295 |
| gross_win_rate | 0.4275 |
| sharpe_ratio | -2.8805 |
| sortino_ratio | -0.6784 |
| max_drawdown | 0.5574 |
| cagr | -0.2686 |
| net_avg_win | 58.6739 |
| net_avg_loss | -78.2583 |
| avg_hold_time_bars | 13.3768 |
| exposure | 0.1678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
