# EMA Hourly Continuation — REQ/USDT P8_100

**Symbol:** REQ/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 883 |
| net_profit_factor | 0.4203 |
| net_win_rate | 0.3805 |
| gross_profit_factor | 0.7592 |
| gross_win_rate | 0.4134 |
| sharpe_ratio | -8.9547 |
| sortino_ratio | -3.7317 |
| max_drawdown | 0.9912 |
| cagr | -0.8467 |
| net_avg_win | 21.3877 |
| net_avg_loss | -31.2545 |
| avg_hold_time_bars | 14.9105 |
| exposure | 0.5985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
