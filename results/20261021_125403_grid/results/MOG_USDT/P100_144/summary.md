# EMA Hourly Continuation — MOG/USDT P100_144

**Symbol:** MOG/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 216 |
| net_profit_factor | 0.7510 |
| net_win_rate | 0.4861 |
| gross_profit_factor | 0.9407 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -1.4003 |
| sortino_ratio | -0.3075 |
| max_drawdown | 0.3181 |
| cagr | -0.1317 |
| net_avg_win | 79.5325 |
| net_avg_loss | -100.1805 |
| avg_hold_time_bars | 6.3102 |
| exposure | 0.0678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
