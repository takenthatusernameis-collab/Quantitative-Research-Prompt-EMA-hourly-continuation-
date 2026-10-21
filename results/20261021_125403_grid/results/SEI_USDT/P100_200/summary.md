# EMA Hourly Continuation — SEI/USDT P100_200

**Symbol:** SEI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.7568 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9462 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -1.2571 |
| sortino_ratio | -0.2798 |
| max_drawdown | 0.3159 |
| cagr | -0.1206 |
| net_avg_win | 72.1400 |
| net_avg_loss | -92.2245 |
| avg_hold_time_bars | 12.7727 |
| exposure | 0.1405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
