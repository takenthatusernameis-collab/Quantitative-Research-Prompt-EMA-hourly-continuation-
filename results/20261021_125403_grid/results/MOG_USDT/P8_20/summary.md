# EMA Hourly Continuation — MOG/USDT P8_20

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7877 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9859 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -1.8936 |
| sortino_ratio | -0.6201 |
| max_drawdown | 0.5063 |
| cagr | -0.2486 |
| net_avg_win | 75.3701 |
| net_avg_loss | -93.7010 |
| avg_hold_time_bars | 5.6806 |
| exposure | 0.1353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
