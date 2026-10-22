# EMA Hourly Continuation — ONE/USDT P12_100

**Symbol:** ONE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.8083 |
| net_win_rate | 0.4883 |
| gross_profit_factor | 0.9646 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -1.4992 |
| sortino_ratio | -0.4413 |
| max_drawdown | 0.4644 |
| cagr | -0.1851 |
| net_avg_win | 81.4664 |
| net_avg_loss | -96.1675 |
| avg_hold_time_bars | 31.2864 |
| exposure | 0.6058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
