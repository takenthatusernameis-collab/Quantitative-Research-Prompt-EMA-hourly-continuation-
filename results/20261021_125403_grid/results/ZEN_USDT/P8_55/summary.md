# EMA Hourly Continuation — ZEN/USDT P8_55

**Symbol:** ZEN/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.7502 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9449 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -2.3003 |
| sortino_ratio | -0.8721 |
| max_drawdown | 0.6439 |
| cagr | -0.3316 |
| net_avg_win | 55.3812 |
| net_avg_loss | -70.7506 |
| avg_hold_time_bars | 14.2567 |
| exposure | 0.4569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
