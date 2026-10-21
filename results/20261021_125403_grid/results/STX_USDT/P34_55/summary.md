# EMA Hourly Continuation — STX/USDT P34_55

**Symbol:** STX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7253 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0079 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -1.6528 |
| sortino_ratio | -0.4148 |
| max_drawdown | 0.4142 |
| cagr | -0.1717 |
| net_avg_win | 64.4508 |
| net_avg_loss | -91.2118 |
| avg_hold_time_bars | 6.2288 |
| exposure | 0.0862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
