# EMA Hourly Continuation — BTT/USDT P12_89

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.4453 |
| net_win_rate | 0.4065 |
| gross_profit_factor | 0.8883 |
| gross_win_rate | 0.4553 |
| sharpe_ratio | -7.3421 |
| sortino_ratio | -2.5672 |
| max_drawdown | 0.9634 |
| cagr | -0.7317 |
| net_avg_win | 30.9274 |
| net_avg_loss | -47.5744 |
| avg_hold_time_bars | 21.9138 |
| exposure | 0.6126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
