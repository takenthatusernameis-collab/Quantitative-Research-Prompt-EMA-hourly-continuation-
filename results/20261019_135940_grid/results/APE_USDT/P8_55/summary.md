# EMA Hourly Continuation — APE/USDT P8_55

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1078 |
| net_profit_factor | 0.6031 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.9443 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -6.4342 |
| sortino_ratio | -2.9765 |
| max_drawdown | 0.9731 |
| cagr | -0.7581 |
| net_avg_win | 30.2523 |
| net_avg_loss | -41.4914 |
| avg_hold_time_bars | 9.8479 |
| exposure | 0.4825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
