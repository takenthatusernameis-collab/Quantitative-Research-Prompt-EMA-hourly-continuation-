# EMA Hourly Continuation — ZRX/USDT P8_12

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1718 |
| net_profit_factor | 0.2725 |
| net_win_rate | 0.3894 |
| gross_profit_factor | 0.8379 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -15.7190 |
| sortino_ratio | -9.4020 |
| max_drawdown | 1.0000 |
| cagr | -0.9922 |
| net_avg_win | 5.5984 |
| net_avg_loss | -13.1033 |
| avg_hold_time_bars | 2.3743 |
| exposure | 0.1854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
