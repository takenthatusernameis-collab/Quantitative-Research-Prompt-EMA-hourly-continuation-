# EMA Hourly Continuation — ERG/USDT P20_200

**Symbol:** ERG/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.5272 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.7711 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -3.9424 |
| sortino_ratio | -1.2014 |
| max_drawdown | 0.7753 |
| cagr | -0.4400 |
| net_avg_win | 40.7222 |
| net_avg_loss | -61.6735 |
| avg_hold_time_bars | 27.1522 |
| exposure | 0.5838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
