# EMA Hourly Continuation — G/USDT P12_20

**Symbol:** G/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1115 |
| net_profit_factor | 0.3006 |
| net_win_rate | 0.4197 |
| gross_profit_factor | 0.7657 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -11.5848 |
| sortino_ratio | -5.9328 |
| max_drawdown | 0.9985 |
| cagr | -0.9503 |
| net_avg_win | 9.1710 |
| net_avg_loss | -22.0669 |
| avg_hold_time_bars | 3.2825 |
| exposure | 0.1924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
