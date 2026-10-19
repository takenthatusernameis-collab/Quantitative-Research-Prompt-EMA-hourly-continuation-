# EMA Hourly Continuation — AKT/USDT P8_20

**Symbol:** AKT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1567 |
| net_profit_factor | 0.4410 |
| net_win_rate | 0.4282 |
| gross_profit_factor | 0.9311 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -11.0941 |
| sortino_ratio | -6.1768 |
| max_drawdown | 0.9996 |
| cagr | -0.9547 |
| net_avg_win | 11.7543 |
| net_avg_loss | -19.9586 |
| avg_hold_time_bars | 2.8673 |
| exposure | 0.2042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
