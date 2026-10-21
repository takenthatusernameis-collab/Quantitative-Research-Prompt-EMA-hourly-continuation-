# EMA Hourly Continuation — ZEC/USDT P8_144

**Symbol:** ZEC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.9656 |
| net_win_rate | 0.5283 |
| gross_profit_factor | 1.1020 |
| gross_win_rate | 0.5283 |
| sharpe_ratio | -0.1339 |
| sortino_ratio | -0.0344 |
| max_drawdown | 0.1629 |
| cagr | -0.0212 |
| net_avg_win | 87.5066 |
| net_avg_loss | -101.4944 |
| avg_hold_time_bars | 52.9969 |
| exposure | 0.7660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
