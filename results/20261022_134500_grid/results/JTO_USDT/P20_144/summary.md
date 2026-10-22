# EMA Hourly Continuation — JTO/USDT P20_144

**Symbol:** JTO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.7158 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.9580 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -2.6756 |
| sortino_ratio | -0.8556 |
| max_drawdown | 0.6730 |
| cagr | -0.3322 |
| net_avg_win | 65.2464 |
| net_avg_loss | -82.7402 |
| avg_hold_time_bars | 23.1470 |
| exposure | 0.5440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
