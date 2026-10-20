# EMA Hourly Continuation — ZRX/USDT P8_26

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1486 |
| net_profit_factor | 0.4320 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.8613 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -9.8133 |
| sortino_ratio | -5.3347 |
| max_drawdown | 0.9986 |
| cagr | -0.9266 |
| net_avg_win | 11.4890 |
| net_avg_loss | -21.3092 |
| avg_hold_time_bars | 4.4717 |
| exposure | 0.3020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
