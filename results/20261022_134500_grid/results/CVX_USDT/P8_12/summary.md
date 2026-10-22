# EMA Hourly Continuation — CVX/USDT P8_12

**Symbol:** CVX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1884 |
| net_profit_factor | 0.2728 |
| net_win_rate | 0.3806 |
| gross_profit_factor | 0.8335 |
| gross_win_rate | 0.4252 |
| sharpe_ratio | -16.6205 |
| sortino_ratio | -10.3151 |
| max_drawdown | 1.0000 |
| cagr | -0.9955 |
| net_avg_win | 5.2310 |
| net_avg_loss | -11.7829 |
| avg_hold_time_bars | 1.9666 |
| exposure | 0.1684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
