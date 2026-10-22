# EMA Hourly Continuation — KNC/USDT P20_144

**Symbol:** KNC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.8442 |
| net_win_rate | 0.5176 |
| gross_profit_factor | 1.0688 |
| gross_win_rate | 0.5176 |
| sharpe_ratio | -1.0188 |
| sortino_ratio | -0.2813 |
| max_drawdown | 0.4017 |
| cagr | -0.1226 |
| net_avg_win | 79.4418 |
| net_avg_loss | -100.9731 |
| avg_hold_time_bars | 35.9919 |
| exposure | 0.6037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
