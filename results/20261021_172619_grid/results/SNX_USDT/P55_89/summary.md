# EMA Hourly Continuation — SNX/USDT P55_89

**Symbol:** SNX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.8943 |
| net_win_rate | 0.5486 |
| gross_profit_factor | 1.2107 |
| gross_win_rate | 0.5486 |
| sharpe_ratio | -0.5983 |
| sortino_ratio | -0.1549 |
| max_drawdown | 0.2682 |
| cagr | -0.0710 |
| net_avg_win | 81.9472 |
| net_avg_loss | -111.3627 |
| avg_hold_time_bars | 6.0690 |
| exposure | 0.0876 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
