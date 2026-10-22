# EMA Hourly Continuation — ETH/USDT P8_100

**Symbol:** ETH/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.5214 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.9313 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -4.9378 |
| sortino_ratio | -1.6061 |
| max_drawdown | 0.8721 |
| cagr | -0.5519 |
| net_avg_win | 37.4750 |
| net_avg_loss | -61.8150 |
| avg_hold_time_bars | 27.7670 |
| exposure | 0.6879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
