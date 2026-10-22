# EMA Hourly Continuation — UQC/USDT P20_100

**Symbol:** UQC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.3538 |
| net_win_rate | 0.2988 |
| gross_profit_factor | 0.5152 |
| gross_win_rate | 0.3227 |
| sharpe_ratio | -5.7675 |
| sortino_ratio | -1.2700 |
| max_drawdown | 0.8106 |
| cagr | -0.4830 |
| net_avg_win | 59.1820 |
| net_avg_loss | -71.2741 |
| avg_hold_time_bars | 51.4821 |
| exposure | 0.5848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
