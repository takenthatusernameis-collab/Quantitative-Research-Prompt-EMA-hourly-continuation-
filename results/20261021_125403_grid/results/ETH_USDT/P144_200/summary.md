# EMA Hourly Continuation — ETH/USDT P144_200

**Symbol:** ETH/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 211 |
| net_profit_factor | 0.5592 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.8814 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -2.4277 |
| sortino_ratio | -0.5077 |
| max_drawdown | 0.4600 |
| cagr | -0.2069 |
| net_avg_win | 55.4360 |
| net_avg_loss | -91.0215 |
| avg_hold_time_bars | 7.7204 |
| exposure | 0.0740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
