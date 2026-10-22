# EMA Hourly Continuation — FIDA/USDT P20_89

**Symbol:** FIDA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.6822 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.8790 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -2.4829 |
| sortino_ratio | -0.8073 |
| max_drawdown | 0.6374 |
| cagr | -0.3102 |
| net_avg_win | 52.2123 |
| net_avg_loss | -70.0878 |
| avg_hold_time_bars | 16.4742 |
| exposure | 0.3899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
