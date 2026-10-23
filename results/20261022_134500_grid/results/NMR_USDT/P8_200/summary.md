# EMA Hourly Continuation — NMR/USDT P8_200

**Symbol:** NMR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6991 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9988 |
| gross_win_rate | 0.5091 |
| sharpe_ratio | -2.1037 |
| sortino_ratio | -0.6185 |
| max_drawdown | 0.5655 |
| cagr | -0.2561 |
| net_avg_win | 56.9088 |
| net_avg_loss | -77.7727 |
| avg_hold_time_bars | 38.7215 |
| exposure | 0.7709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
