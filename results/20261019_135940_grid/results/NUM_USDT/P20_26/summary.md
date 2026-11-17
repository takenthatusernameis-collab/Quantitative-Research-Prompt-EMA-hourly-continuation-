# EMA Hourly Continuation — NUM/USDT P20_26

**Symbol:** NUM/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1121 |
| net_profit_factor | 0.1913 |
| net_win_rate | 0.2953 |
| gross_profit_factor | 0.6586 |
| gross_win_rate | 0.3399 |
| sharpe_ratio | -15.5702 |
| sortino_ratio | -7.6186 |
| max_drawdown | 1.0000 |
| cagr | -0.9822 |
| net_avg_win | 7.1449 |
| net_avg_loss | -15.6513 |
| avg_hold_time_bars | 2.9768 |
| exposure | 0.1517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
