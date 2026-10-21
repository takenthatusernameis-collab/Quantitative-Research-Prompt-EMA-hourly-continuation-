# EMA Hourly Continuation — BTT/USDT P34_100

**Symbol:** BTT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.5143 |
| net_win_rate | 0.4301 |
| gross_profit_factor | 0.8300 |
| gross_win_rate | 0.4326 |
| sharpe_ratio | -4.8180 |
| sortino_ratio | -1.3568 |
| max_drawdown | 0.8018 |
| cagr | -0.4725 |
| net_avg_win | 50.9852 |
| net_avg_loss | -74.8073 |
| avg_hold_time_bars | 16.9482 |
| exposure | 0.2974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
