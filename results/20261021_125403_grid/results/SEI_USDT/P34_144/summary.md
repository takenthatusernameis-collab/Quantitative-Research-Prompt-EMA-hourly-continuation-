# EMA Hourly Continuation — SEI/USDT P34_144

**Symbol:** SEI/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.8456 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 1.0114 |
| gross_win_rate | 0.5048 |
| sharpe_ratio | -0.8979 |
| sortino_ratio | -0.2270 |
| max_drawdown | 0.2589 |
| cagr | -0.1011 |
| net_avg_win | 81.8667 |
| net_avg_loss | -98.7057 |
| avg_hold_time_bars | 30.4534 |
| exposure | 0.4305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
