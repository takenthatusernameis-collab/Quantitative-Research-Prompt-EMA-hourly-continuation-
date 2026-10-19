# EMA Hourly Continuation — ENS/USDT P21_26

**Symbol:** ENS/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1237 |
| net_profit_factor | 0.2684 |
| net_win_rate | 0.3436 |
| gross_profit_factor | 0.7339 |
| gross_win_rate | 0.3921 |
| sharpe_ratio | -15.5801 |
| sortino_ratio | -8.0139 |
| max_drawdown | 1.0000 |
| cagr | -0.9876 |
| net_avg_win | 8.6307 |
| net_avg_loss | -16.8324 |
| avg_hold_time_bars | 1.9757 |
| exposure | 0.1111 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
