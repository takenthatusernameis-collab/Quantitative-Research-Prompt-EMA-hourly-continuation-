# EMA Hourly Continuation — CVX/USDT P20_55

**Symbol:** CVX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 966 |
| net_profit_factor | 0.4962 |
| net_win_rate | 0.4389 |
| gross_profit_factor | 0.7943 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -6.7219 |
| sortino_ratio | -2.9431 |
| max_drawdown | 0.9728 |
| cagr | -0.7605 |
| net_avg_win | 22.5910 |
| net_avg_loss | -35.6130 |
| avg_hold_time_bars | 5.3364 |
| exposure | 0.2343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
