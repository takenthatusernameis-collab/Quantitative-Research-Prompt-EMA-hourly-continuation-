# EMA Hourly Continuation — ZRX/USDT P20_21

**Symbol:** ZRX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1206 |
| net_profit_factor | 0.1506 |
| net_win_rate | 0.3118 |
| gross_profit_factor | 0.7299 |
| gross_win_rate | 0.4270 |
| sharpe_ratio | -16.9721 |
| sortino_ratio | -8.8711 |
| max_drawdown | 1.0000 |
| cagr | -0.9922 |
| net_avg_win | 4.7153 |
| net_avg_loss | -14.1842 |
| avg_hold_time_bars | 2.1534 |
| exposure | 0.1180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
