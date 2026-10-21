# EMA Hourly Continuation — ERG/USDT P21_55

**Symbol:** ERG/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6631 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.8949 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -2.7922 |
| sortino_ratio | -0.8314 |
| max_drawdown | 0.6340 |
| cagr | -0.3176 |
| net_avg_win | 59.5332 |
| net_avg_loss | -79.2824 |
| avg_hold_time_bars | 9.1586 |
| exposure | 0.1811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
