# EMA Hourly Continuation — ONE/USDT P100_200

**Symbol:** ONE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.7647 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9384 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -1.3269 |
| sortino_ratio | -0.2947 |
| max_drawdown | 0.3033 |
| cagr | -0.1273 |
| net_avg_win | 80.4361 |
| net_avg_loss | -98.4560 |
| avg_hold_time_bars | 18.0909 |
| exposure | 0.1990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
