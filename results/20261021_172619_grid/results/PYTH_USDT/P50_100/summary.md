# EMA Hourly Continuation — PYTH/USDT P50_100

**Symbol:** PYTH/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.6921 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.8684 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -2.0513 |
| sortino_ratio | -0.5460 |
| max_drawdown | 0.4779 |
| cagr | -0.2221 |
| net_avg_win | 64.0993 |
| net_avg_loss | -82.1059 |
| avg_hold_time_bars | 8.7794 |
| exposure | 0.1393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
